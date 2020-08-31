# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter


from .api import (
    LocationViewSet, UsersLocationViewSet
)

router = DefaultRouter()

router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'locations/(?P<location_pk>\d+)/users', UsersLocationViewSet, basename='locations-users')

urlpatterns = []

urlpatterns += router.urls
