# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.devices.api import (
    DeviceViewSet,
    DeviceAttributeViewSet,
    EventStateViewSet,
    EventActionViewSet
)

router = DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='devices')
router.register(r'devices/(?P<device_pk>[0-9a-f-]+)/attributes',
                DeviceAttributeViewSet, basename='devices-attrs')
router.register(r'components/(?P<device_pk>[0-9a-f-]+)/events-state',
                EventStateViewSet, basename='components-events-state')
router.register(r'components/(?P<device_pk>[0-9a-f-]+)/events-action',
                EventActionViewSet, basename='components-events-action')

urlpatterns = [
    url(r'^devices/(?P<device_pk>[0-9a-f-]+)/components/',
        include(('apps.devices.components.urls', 'components'), namespace='devices')),
]

urlpatterns += router.urls
