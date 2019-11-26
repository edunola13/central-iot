# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from apps.components.api import SensorViewSet, ActuatorViewSet, ControllerViewSet

router = DefaultRouter()
router.register(r'sensors', SensorViewSet, base_name='sensors')
router.register(r'actuators', ActuatorViewSet, base_name='devices')
router.register(r'controllers', ControllerViewSet, base_name='controllers')

urlpatterns = router.urls
