# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from devices.models import Device
from sensors.models import Sensor
from devices.serializers import DeviceSerializer
from sensors.serializers import SensorSerializer
from RobotApiRest.permissions import AutomatizadorOrReadOnly


class DeviceList(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    __basic_fields = ('code', 'deviceType')
    filter_fields = __basic_fields
    search_fields = __basic_fields


class DeviceDetail(generics.RetrieveUpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (IsAuthenticated, AutomatizadorOrReadOnly, )

@api_view(['GET'])
def devices_sensor(request):
    devices = Device.objects.filter(deviceType=Device.TYPE_SENSOR)
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def devices_actuator(request):
    devices = Device.objects.filter(deviceType=Device.TYPE_ACTUATOR)
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sensors_of_devices(request, pk):
    device = None
    try:
        device = Device.objects.filter(deviceType=Device.TYPE_SENSOR).get(pk=pk)
    except Device.DoesNotExist:
        raise Http404
    sensors = Sensor.objects.filter(device_id=pk)
    serializer = SensorSerializer(sensors, many=True)
    return Response(serializer.data)
