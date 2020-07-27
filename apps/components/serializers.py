# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from apps.components.models import Sensor, Actuator, Controller

from apps.devices.serializers import DeviceSerializer


class ComponentSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()


class SensorSerializer(ComponentSerializer):
    status_data = serializers.SerializerMethodField()

    class Meta:
        model = Sensor
        fields = '__all__'

    def get_status_data(self, obj):
        return obj.get_status_data()


class SensorUpdateSerializer(ComponentSerializer):

    class Meta:
        model = Sensor
        fields = ('name', 'enabled')


class ActuatorSerializer(ComponentSerializer):
    status_data = serializers.SerializerMethodField()

    class Meta:
        model = Actuator
        fields = '__all__'

    def get_status_data(self, obj):
        return obj.get_status_data()


class ActuatorUpdateSerializer(ComponentSerializer):

    class Meta:
        model = Actuator
        fields = ('name', 'enabled')


class ControllerSerializer(ComponentSerializer):
    status_data = serializers.SerializerMethodField()

    class Meta:
        model = Controller
        fields = '__all__'

    def get_status_data(self, obj):
        return obj.get_status_data()


class ControllerUpdateSerializer(ComponentSerializer):

    class Meta:
        model = Controller
        fields = ('name', 'enabled')
