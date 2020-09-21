# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from .api import (
    ManufacterViewSet,
)

from .api_admin import (
    AdminManufacterViewSet,
    AdminManufacterConfigViewSet
)

router = DefaultRouter()
# Public
router.register(r'public/manufacters', ManufacterViewSet, basename='manufacters')
# Admin
router.register(r'admin/manufacters', AdminManufacterViewSet, basename='manufacters')
router.register(r'admin/manufacters/(?P<manu_pk>\d+)/config', AdminManufacterConfigViewSet, basename='manufacters_config')

urlpatterns = router.urls
