# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.devices.api import (
    DeviceViewSet,
    DeviceAttributeViewSet,
    EventStateViewSet,
    EventActionViewSet
)

router = DefaultRouter()
router.register('devices', DeviceViewSet, basename='devices')
router.register(r'devices/(?P<device_pk>\d+)/attributes',
                DeviceAttributeViewSet, basename='devices-attrs')
router.register(r'devices/(?P<device_pk>\d+)/events-state',
                EventStateViewSet, basename='devices-events-state')
router.register(r'devices/(?P<device_pk>\d+)/events-action',
                EventActionViewSet, basename='devices-events-action')

urlpatterns = [
    path('devices/<int:device_pk>/components/',
        include(('apps.devices.components.urls', 'components'), namespace='devices')),
]

urlpatterns += router.urls
