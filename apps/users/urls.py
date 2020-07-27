# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from apps.users.api import (
    UserViewSet, GroupViewSet,
    CurrentUserView
)

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'groups', GroupViewSet, base_name='groups')
urlpatterns = [
    url(r'^users/current/$', CurrentUserView.as_view()),
]

urlpatterns += router.urls
