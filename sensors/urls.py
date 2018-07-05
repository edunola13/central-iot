from sensors.views import SensorViewSet, SensorReadingRead
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sensors', SensorViewSet, base_name='sensors')
router.register(r'sensors_reading', SensorReadingRead, base_name='sensors_reading')
urlpatterns = router.urls