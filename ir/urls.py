from ir.views import IrControlViewSet, IrActionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ir_controls', IrControlViewSet, base_name='ir_controls')
router.register(r'ir_actions', IrActionViewSet, base_name='ir_actions')
urlpatterns = router.urls