# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from sensors.models import Sensor, SensorReading
from apps.devices.models import Device
from apps.devices.serializers import DeviceSerializer


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('id', 'code', 'name', 'sensorType', 'lastRead', 'lastUpdate', 'created', 'device')
        read_only_fields = ('code', 'sensorType', 'lastRead', 'lastUpdate', 'device')

class SensorDetailSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(many=False, read_only=True)

    class Meta:
        model = Sensor
        fields = ('id', 'code', 'name', 'sensorType', 'lastRead', 'lastUpdate', 'created', 'device')
        read_only_fields = ('code', 'sensorType', 'lastRead', 'lastUpdate')


class SensorReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorReading
        fields = ('id', 'read', 'created')
        read_only_fields = ('read',)

class SensorReadingDetailSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(many=False, read_only=True)

    class Meta:
        model = SensorReading
        fields = ('id', 'read', 'sensor', 'created')
        read_only_fields = ('read',)