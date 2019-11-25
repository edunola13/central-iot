# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from apps.devices.models import Device


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('id', 'name', 'device_type', 'version', 'device_id',
                  'address', 'status', 'last_connection', 'enabled',
                  'created_at', 'updated_at')
        read_only_fields = (
            'id', 'device_type', 'status', 'device_id',
            'last_connection', 'created_at', 'updated_at')
