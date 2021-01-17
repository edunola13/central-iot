# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path

from .api import (
    RegisterDeviceView,
)


urlpatterns = [
    path('devices/', RegisterDeviceView.as_view(), name='register'),
]
