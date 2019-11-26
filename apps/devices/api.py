# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.utils.permissions import SafeMethodOrIsStaff

from apps.devices.models import Device
from apps.devices.serializers import DeviceSerializer


class DeviceViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    permission_classes = (SafeMethodOrIsStaff,)

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    __basic_fields = ('name',)
    filter_fields = __basic_fields + (
        'device_type', 'version', 'last_connection', 'enabled', 'status',)
    search_fields = __basic_fields + ('device_id',)
    ordering_fields = __basic_fields + ('created_at',)
    ordering = 'name'

    @action(methods=['post'], detail=False)
    def search_device(self, request, pk=None):
        # DATA = {'device_type': 'X'}

        # SEARCH IN ALL IPs
        # CREATE DEVICE AND COMPONENTS

        serializer = DeviceSerializer()

        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, permission_classes=(IsAuthenticated,))
    def refresh_status(self, request, pk=None):
        # Refresca el estado pidiendolo

        serializer = DeviceSerializer()

        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, permission_classes=(IsAuthenticated,))
    def refresh_components(self, request, pk=None):
        # Refresca los componentes pidiendolo

        serializer = DeviceSerializer()

        return Response(serializer.data,
                        status=status.HTTP_200_OK)
