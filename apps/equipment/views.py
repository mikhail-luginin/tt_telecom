from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import EquipmentType, Equipment
from .serializers import EquipmentTypeSerializer, EquipmentSerializer


class EquipmentTypeViewSet(ModelViewSet):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = self.queryset
        name = self.request.query_params.get('name')

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = self.queryset
        equipment_id = self.request.query_params.get('id')
        equipment_type = self.request.query_params.get('equipment_type')
        serial_number = self.request.query_params.get('serial_number')
        note = self.request.query_params.get('note')
        is_deleted = self.request.query_params.get('is_deleted')

        filter_params = dict(
            id=equipment_id,
            equipment_type=equipment_type,
            serial_number=serial_number,
            note=note,
            is_deleted=is_deleted
        )

        for k, v in list(filter_params.items()):
            if v is None:
                filter_params.pop(k)

        if len(filter_params) > 0:
            queryset = queryset.filter(**filter_params)

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()

        return Response(status=204)
