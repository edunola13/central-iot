# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from apps.devices.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    status_data = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = ('id', 'name', 'device_type', 'version', 'device_id',
                  'address', 'status', 'status_data', 'last_connection', 'enabled',
                  'created_at', 'updated_at')
        read_only_fields = (
            'id', 'device_type', 'version', 'status', 'status_data', 'device_id',
            'last_connection', 'created_at', 'updated_at')

    def get_status_data(self, obj):
        return obj.get_status_data()
