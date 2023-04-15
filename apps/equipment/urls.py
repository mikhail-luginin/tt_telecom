from rest_framework.routers import SimpleRouter

from .views import EquipmentTypeViewSet, EquipmentViewSet


router = SimpleRouter()
router.register(r'equipment', EquipmentViewSet)
router.register(r'equipment-type', EquipmentTypeViewSet)

urlpatterns = router.urls
