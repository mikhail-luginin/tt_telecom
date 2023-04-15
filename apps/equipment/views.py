from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

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
    http_method_names = ['get']
