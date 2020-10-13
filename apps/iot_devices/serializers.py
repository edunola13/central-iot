# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _

from rest_framework import serializers

from apps.locations.models import Location

from .constants import (
    MODEL_TYPE_CHOICES,
    MODEL_TYPE_RELAYS
)


class RegisterDeviceSerializer(serializers.Serializer):
    device_id = serializers.UUIDField()
    model_type = serializers.ChoiceField(choices=MODEL_TYPE_CHOICES)
    version = serializers.CharField(max_length=10)
    secret_key = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), write_only=True, many=False, required=False
    )

    @classmethod
    def get_for_type(cls, model_type):
        serializers = {
            MODEL_TYPE_RELAYS: RegisterDeviceRelaysSerializer,
        }
        return serializers.get(model_type, RegisterDeviceSerializer)


class RegisterDeviceRelaysSerializer(RegisterDeviceSerializer):
    relays = serializers.IntegerField(min_value=1, default=1)


class UnregisterDeviceSerializer(serializers.Serializer):
    device_id = serializers.UUIDField()
    secret_key = serializers.CharField(max_length=10)
