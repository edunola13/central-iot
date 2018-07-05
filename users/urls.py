from users.views import UserViewSet, GroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'groups', GroupViewSet, base_name='groups')
urlpatterns = router.urls