from rest_framework_simplejwt.views import TokenObtainPairView

from .models import EquipmentType, Equipment
from .serializers import EquipmentTypeSerializer, EquipmentSerializer, TokenSerializer
from .utils import ModelViewSetMixin


class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer


class EquipmentTypeViewSet(ModelViewSetMixin):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    http_method_names = ['get']
    queryset_fields = ['name']


class EquipmentViewSet(ModelViewSetMixin):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset_fields = ['equipment_type', 'serial_number', 'note', 'is_deleted']
