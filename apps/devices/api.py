# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from rest_framework import status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.utils.permissions import SafeMethodOrIsStaff

from apps.devices.models import Device
from apps.data_history.models import DataHistory

from apps.devices.serializers import DeviceSerializer
from apps.data_history.serializers import DataHistorySerializer


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

    @action(methods=['post'], detail=False, permission_classes=(IsAuthenticated,))
    def search_device(self, request, pk=None):
        data = request.data

        device = Device.add_device_from_network(request.META['REMOTE_ADDR'], data.get('device_type'))
        if device is None:
            raise Http404

        serializer = DeviceSerializer(device)

        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, permission_classes=(IsAuthenticated,))
    def refresh_status(self, request, pk=None):
        instance = self.get_object()
        instance.refresh_status_data()

        serializer = DeviceSerializer(instance)

        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, permission_classes=(IsAuthenticated,))
    def refresh_components(self, request, pk=None):
        instance = self.get_object()
        instance.refresh_components()

        serializer = DeviceSerializer(instance)

        return Response(serializer.data,
                        status=status.HTTP_200_OK)


class DataHistoryDeviceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = (SafeMethodOrIsStaff,)

    queryset = DataHistory.objects.all()
    serializer_class = DataHistorySerializer

    __basic_fields = ('created_at',)
    filter_fields = __basic_fields
    ordering_fields = __basic_fields
    ordering = '-created_at'

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DataHistory.objects.all()

        ct = ContentType.objects.get_for_model(Device)
        return DataHistory.objects.filter(
            content_type=ct,
            object_id=self.kwargs["device_pk"]
        )
