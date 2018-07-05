# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from devices.models import Device


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('id', 'code', 'name', 'deviceType', 'created')
        read_only_fields = ('code', 'deviceType')