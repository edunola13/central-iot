# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from .api import (
    ComponentViewSet,
    EventStateViewSet,
    EventActionViewSet,
)

router = DefaultRouter()
router.register(r'components', ComponentViewSet, basename='components')
router.register(r'components/(?P<com_pk>[0-9a-f-]+)/events-state',
                EventStateViewSet, basename='components-events-state')
router.register(r'components/(?P<com_pk>[0-9a-f-]+)/events-action',
                EventActionViewSet, basename='components-events-action')

urlpatterns = router.urls
