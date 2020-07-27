# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.utils.permissions import SafeMethodOrIsStaff

from apps.components.models import Sensor, Actuator, Controller

from apps.components.serializers import (
    SensorSerializer, SensorUpdateSerializer,
    ActuatorSerializer, ActuatorUpdateSerializer,
    ControllerSerializer, ControllerUpdateSerializer
)


class SensorViewSet(ReadOnlyModelViewSet):
    permission_classes = (SafeMethodOrIsStaff,)

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    __basic_fields = ('name',)
    filter_fields = __basic_fields + (
        'component_type', 'sensor_type', 'record_history', 'enabled', 'device'
    )
    search_fields = __basic_fields
    ordering_fields = __basic_fields + ('created_at', 'updated_at')
    ordering = 'name'

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = SensorUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    @action(methods=['put'], detail=True, permission_classes=(IsAuthenticated,))
    def refresh(self, request, pk=None):
        # Refresca el componente pidiendolo

        serializer = SensorSerializer()

        return Response(serializer.data,
                        status=status.HTTP_200_OK)


class ActuatorViewSet(ReadOnlyModelViewSet):
    # permission_classes = (IsAdminUser,)

    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer

    __basic_fields = ('name',)
    filter_fields = __basic_fields + (
        'component_type', 'actuator_type', 'record_history', 'enabled', 'device'
    )
    search_fields = __basic_fields
    ordering_fields = __basic_fields + ('created_at', 'updated_at')
    ordering = 'name'

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ActuatorUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    @action(methods=['put'], detail=True, permission_classes=(IsAuthenticated,))
    def refresh(self, request, pk=None):
        # Refresca el componente pidiendolo

        serializer = ActuatorSerializer()

        return Response(serializer.data,
                        status=status.HTTP_200_OK)


class ControllerViewSet(ReadOnlyModelViewSet):
    # permission_classes = (IsAdminUser,)

    queryset = Controller.objects.all()
    serializer_class = ControllerSerializer

    __basic_fields = ('name',)
    filter_fields = __basic_fields + (
        'component_type', 'controller_type', 'record_history', 'enabled', 'device'
    )
    search_fields = __basic_fields
    ordering_fields = __basic_fields + ('created_at', 'updated_at')
    ordering = 'name'

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ControllerUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    @action(methods=['put'], detail=True, permission_classes=(IsAuthenticated,))
    def refresh(self, request, pk=None):
        # Refresca el componente pidiendolo

        serializer = ControllerSerializer()

        return Response(serializer.data,
                        status=status.HTTP_200_OK)
