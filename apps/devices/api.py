# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.utils.translation import ugettext as _

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action

from django_module_common.utils.exceptions import ConflictError
from django_module_common.utils.pagination import MongoPagination

from .models import (
    Device
)
from django_module_attr.models import Attribute
from apps.components.models_md import EventState, EventAction

from apps.devices.clients.proxy_manufacter import ProxyManufacter

from .serializers import (
    DeviceSerializer, DeviceCreateSerializer,
    DeviceActionSerializer,
    AttributeSerializer
)
from apps.components.serializers import (
    EventStateSerializer,
    EventActionSerializer
)
from commons.utils.serializers import MetadataSerializer

from apps.components.filters import EventStateFilter, EventActionFilter


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all().select_related('metadata', 'location', 'manufacter')
    serializer_class = DeviceSerializer

    filter_fields = {
        'external_id': ['exact'],
        'type': ['exact'],
        'enabled': ['exact'],
        'location': ['exact'],
        'manufacter': ['exact']
    }
    search_fields = ('name')
    ordering_fields = ('name', 'order', 'created_at')
    ordering = 'name'

    def get_queryset(self):
        return self.queryset.filter(
            location__users__user=self.request.user,
            location__users__enabled=True
        )

    # CHECK PERMISSIONS

    def create(self, request, *args, **kwargs):
        serializer = DeviceCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # VALIDATE LOCATION PERMISSION

        device = serializer.create(
            serializer.validated_data,
        )

        serializer = self.get_serializer(device)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            instance.remove()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            raise ConflictError(detail=_('No se puede eliminar el dispositivo'))

    # CHANGE LOCATION

    # CHANGE CONTAINER

    @action(methods=['put'], detail=False)
    def metadata(self, request):
        instance = self.get_object()

        serializer = MetadataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        metadata = instance.metadata.get_value()
        metadata['config'] = serializer.validated_data['config_metadata']
        instance.metadata.update_value(metadata)

        return Response(
            instance.metadata.get_value(),
            status=status.HTTP_200_OK
        )

    @action(methods=['post'], detail=False)
    def sync(self, request):
        instance = self.get_object()

        ProxyManufacter.execute_sync(instance)

        return Response(
            status=status.HTTP_200_OK
        )

    @action(methods=['post'], detail=False)
    def action(self, request):
        instance = self.get_object()
        # Validate the action data against Component Type
        serializer_class = DeviceActionSerializer.get_for_type(instance.type)
        serializer = serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        ProxyManufacter.execute_action(instance, serializer.validated_data, request.user)

        return Response(
            status=status.HTTP_200_OK
        )


class DeviceAttributeViewSet(ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

    ordering = ['name']

    # CHECK PERMISSIONS

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Attribute.objects.all()

        device = Device.objects.get(
            pk=self.kwargs['device_pk'],
            location__users__user=self.request.user
        )
        return device.attrs

    def create(self, request, *args, **kwargs):
        device = Device.objects.get(
            pk=self.kwargs['device_pk'],
            location__users__user=self.request.user
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(device=device)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
            'device': self.kwargs['device_pk']
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
            'device': self.kwargs['device_pk']
        }

        filters = EventActionFilter(data=request.query_params)
        filters.is_valid(raise_exception=True)
        queryset = filters.filter(queryset, query)

        pagination = MongoPagination()
        pagination.paginate_queryset(queryset, self.request.query_params)

        queryset = EventAction.map_objects(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return pagination.paginated_response(serializer.data)
