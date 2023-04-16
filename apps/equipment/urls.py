from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import EquipmentTypeViewSet, EquipmentViewSet, TokenView


router = SimpleRouter()
router.register(r'equipment', EquipmentViewSet)
router.register(r'equipment-type', EquipmentTypeViewSet)

urlpatterns = [
    path('login', TokenView.as_view())
] + router.urls
