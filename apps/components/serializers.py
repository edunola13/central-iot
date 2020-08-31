# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _

from rest_framework import serializers

from django_module_common.utils.serializers import JSONField

from .constants import (
    TYPE_OTHER, TYPE_ON_OFF
)

from .models import Component

from apps.devices.serializers import DeviceMinSerializer
from django_module_attr.serializers import TagSerializer


class ComponentSerializer(serializers.ModelSerializer):
    metadata = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    device = DeviceMinSerializer(many=False, read_only=True)

    class Meta:
        model = Component
        fields = ('id', 'external_id', 'name', 'type',
                  'metadata', 'tags', 'device',
                  'enabled', 'created_at', 'updated_at')

    def get_metadata(self, obj):
        if obj.metadata:
            return obj.metadata.get_value()

        return None


class ComponentActionSerializer(serializers.Serializer):

    @classmethod
    def get_for_type(cls, order_type):
        serializers = {
            TYPE_OTHER: ComponentActionOtherSerializer,
            TYPE_ON_OFF: ComponentActionOnOffSerializer,
        }
        return serializers.get(order_type, None)

    def validate(self, data):
        if not self.instance.device.enabled or not self.instance.enabled:
            raise serializers.ValidationError(_('El dispositivo/componente se encuentra deshabilitado'))

        return data


class ComponentActionOtherSerializer(ComponentActionSerializer):
    data = JSONField()


class ComponentActionOnOffSerializer(ComponentActionSerializer):
    value = serializers.BooleanField()


class EventStateSerializer(serializers.Serializer):
    _id = serializers.CharField()
    device = serializers.CharField()
    component = serializers.CharField()
    type = serializers.CharField()
    payload = serializers.JSONField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class EventActionSerializer(serializers.Serializer):
    _id = serializers.CharField()
    device = serializers.CharField()
    component = serializers.CharField()
    user = serializers.CharField()
    type = serializers.CharField()
    payload = serializers.JSONField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
