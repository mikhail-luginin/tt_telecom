from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.response import Response

from .models import EquipmentType, Equipment
from .services.validators import validate_serial_number


class EquipmentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    equipment_type_name = serializers.CharField(source='equipment_type.name', read_only=True)
    serial_number = serializers.CharField(max_length=500)
    errors = serializers.DictField(read_only=True)
    created_rows = serializers.ListField(read_only=True, child=serializers.CharField())

    class Meta:
        model = Equipment
        fields = ['id', 'equipment_type_name', 'equipment_type', 'serial_number', 'note', 'is_deleted',
                  'errors', 'created_rows']

    def create(self, validated_data):
        serial_numbers = validated_data.get('serial_number')

        if self.is_valid():
            if serial_numbers.startswith('['):
                serial_numbers = eval(serial_numbers)
            if isinstance(serial_numbers, list):
                equipment_type = validated_data.get('equipment_type')
                serial_number_mask = equipment_type.sn_mask
                note = validated_data.get('note')
                equipment_list = []
                error_messages = dict()
                for serial_number in serial_numbers:
                    if validate_serial_number(serial_number_mask, serial_number) is False:
                        error_messages[serial_number] = f'Serial number is not match mask {serial_number_mask}.'
                        continue
                    if Equipment.objects.filter(serial_number=serial_number).exists():
                        error_messages[serial_number] = 'Serial number already exists.'
                        continue
                    equipment_list.append(
                        Equipment(
                            equipment_type=equipment_type,
                            serial_number=serial_number,
                            note=note,
                            is_deleted=False
                        )
                    )
                if equipment_list:
                    rows = Equipment.objects.bulk_create(equipment_list)
                    validated_data['errors'] = error_messages
                    validated_data['created_rows'] = [model_to_dict(row) for row in rows]
                    return validated_data
                if error_messages:
                    raise serializers.ValidationError(error_messages)
            else:
                raise serializers.ValidationError('Field serial_number must be a list')
        else:
            return self.errors
