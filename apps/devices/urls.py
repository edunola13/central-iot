# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from apps.devices.api import DeviceViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet, base_name='devices')

urlpatterns = router.urls
