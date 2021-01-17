# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.conf.urls import url
from rest_framework.routers import DefaultRouter


from .api import (
    ComponentViewSet,
)

router = DefaultRouter()

router.register('', ComponentViewSet, basename='components')

urlpatterns = []

urlpatterns += router.urls
