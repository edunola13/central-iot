# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from apps.ir.api import IrControlViewSet, IrActionViewSet

router = DefaultRouter()
router.register(r'ir_controls', IrControlViewSet, base_name='ir_controls')
router.register(r'ir_actions', IrActionViewSet, base_name='ir_actions')

urlpatterns = router.urls
