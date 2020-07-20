# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from apps.devices.api import DeviceViewSet, DataHistoryDeviceViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet, base_name='devices')
router.register(r'devices/(?P<device_pk>[0-9]+)/history', DataHistoryDeviceViewSet, base_name='device_history')


urlpatterns = router.urls
