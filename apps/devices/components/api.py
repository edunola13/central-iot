# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.db import transaction

from django_module_common.utils.exceptions import ConflictError

from apps.components.models import Component
from apps.devices.models import Device

from .serializers import (
    ComponentSerializer, ComponentCreateSerializer
)
from commons.utils.serializers import MetadataSerializer


class ComponentViewSet(ModelViewSet):
    queryset = Component.objects.all().select_related("metadata").prefetch_related('tags')
    serializer_class = ComponentSerializer

    filter_fields = ('external_id', 'type', 'enabled', 'tags')
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at')
    ordering = 'name'

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Component.objects.all()

        return Component.objects.filter(device__pk=self.kwargs['device_pk'])

    # CHECK PERMISSIONS

    def create(self, request, *args, **kwargs):
        serializer = ComponentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #
        # VALIDATE_UNIQUE: EXTERNAL_ID, DEVICE
        #

        serializer.validated_data.update(device=Device.objects.get(pk=self.kwargs['device_pk']))
        component = serializer.create(
            serializer.validated_data,
        )

        serializer = self.get_serializer(component)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            with transaction.atomic():
                instance.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            raise ConflictError(detail=_('No se puede eliminar el componente'))

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
