# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.data_history.models import DataHistory
from apps.data_history.serializers import DataHistorySerializer

from apps.data_history.filters import DataHistoryFilter


class DataHistoryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = DataHistory.objects.all().select_related('content_type')
    serializer_class = DataHistorySerializer

    filterset_class = DataHistoryFilter
    ordering_fields = ('created_at',)
    ordering = '-created_at'
