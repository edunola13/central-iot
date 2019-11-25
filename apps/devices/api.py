# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.devices.models import Device

from apps.devices.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAdminUser,)

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

        serializer = DeviceSerializer()

        return Response(serializer.data,
                        status=status.HTTP_200_OK)
