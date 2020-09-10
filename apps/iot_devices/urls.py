# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .api import (
    RegisterDeviceView,
)


urlpatterns = [
    url(r'^device/$', RegisterDeviceView.as_view(), name='register'),
]
