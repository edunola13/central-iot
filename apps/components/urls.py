# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from .api import (
    ComponentViewSet,
    EventStateViewSet,
    EventActionViewSet,
)

router = DefaultRouter()
router.register('components', ComponentViewSet, basename='components')
router.register(r'components/(?P<com_pk>\d+)/events-state',
                EventStateViewSet, basename='components-events-state')
router.register(r'components/(?P<com_pk>\d+)/events-action',
                EventActionViewSet, basename='components-events-action')

urlpatterns = router.urls
