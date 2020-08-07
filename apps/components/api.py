# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from django_module_common.utils.pagination import MongoPagination

from .models import Component
from .models_md import EventState, EventAction

from apps.components.serializers import (
    ComponentSerializer,
    EventStateSerializer, EventActionSerializer
)

from .filters import EventStateFilter, EventActionFilter


class ComponentViewSet(ReadOnlyModelViewSet):
    queryset = Component.objects.all().select_related("metadata").prefetch_related('tags')
    serializer_class = ComponentSerializer

    filter_fields = ('external_id', 'type', 'enabled', 'tags', 'device')
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at')
    ordering = 'name'

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Component.objects.all()

        return Component.objects.filter(
            device__location__users__user=self.request.user,
            device__location__users__enabled=True
        )


class EventStateViewSet(GenericViewSet):
    serializer_class = EventStateSerializer

    def get_object(self):
        try:
            return EventState.get_object(self.kwargs['pk'])
        except:
            raise Http404

    # CHECK PERMISSIONS

    def list(self, request, *args, **kwargs):
        queryset = EventState.get_collection()
        query = {
            'component': self.kwargs['com_pk']
        }

        filters = EventStateFilter(data=request.query_params)
        filters.is_valid(raise_exception=True)
        queryset = filters.filter(queryset, query)

        pagination = MongoPagination()
        pagination.paginate_queryset(queryset, self.request.query_params)

        queryset = EventState.map_objects(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return pagination.paginated_response(serializer.data)


class EventActionViewSet(GenericViewSet):
    serializer_class = EventActionSerializer

    def get_object(self):
        try:
            return EventAction.get_object(self.kwargs['pk'])
        except:
            raise Http404

    # CHECK PERMISSIONS

    def list(self, request, *args, **kwargs):
        queryset = EventAction.get_collection()
        query = {
            'component': self.kwargs['com_pk']
        }

        filters = EventActionFilter(data=request.query_params)
        filters.is_valid(raise_exception=True)
        queryset = filters.filter(queryset, query)

        pagination = MongoPagination()
        pagination.paginate_queryset(queryset, self.request.query_params)

        queryset = EventAction.map_objects(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return pagination.paginated_response(serializer.data)
