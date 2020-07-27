# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from apps.data_history.api import DataHistoryViewSet

router = DefaultRouter()
router.register(r'data_history', DataHistoryViewSet, base_name='data_history')

urlpatterns = router.urls
