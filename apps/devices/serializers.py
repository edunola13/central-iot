# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction

from rest_framework import serializers

from .models import Device
from apps.components.models import Component
from apps.locations.models import Location
from django_module_attr.models import Attribute

from apps.locations.serializers import LocationMinSerializer


class DeviceMinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('id', 'external_id', 'name', 'type', 'status',
                  'metadata', 'container', 'location',
                  'enabled', 'created_at', 'updated_at')


class DeviceSerializer(serializers.ModelSerializer):
    metadata = serializers.SerializerMethodField()
    location = LocationMinSerializer()

    class Meta:
        model = Device
        fields = ('id', 'external_id', 'name', 'type', 'status',
                  'metadata', 'container', 'location',
                  'enabled', 'created_at', 'updated_at')
        read_only_fields = ('id', 'status', 'metadata', 'container',
                            'location', 'created_at', 'updated_at')

    def get_metadata(self, obj):
        if obj.metadata:
            return obj.metadata.get_value()

        return None


class AttributeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = ('name', 'value')


class ComponentCreateSerializer(serializers.ModelSerializer):
    # metadata = JSONField(required=False)

    class Meta:
        model = Component
        fields = ('external_id', 'name', 'type')


class DeviceCreateSerializer(serializers.ModelSerializer):
    # metadata = JSONField(required=False)
    attrs = AttributeCreateSerializer(many=True, allow_empty=True)
    components = ComponentCreateSerializer(many=True, allow_empty=True)
    container = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(), write_only=True, many=False, required=False
    )
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), write_only=True, many=False, required=False
    )

    class Meta:
        model = Device
        fields = ('external_id', 'name', 'type',
                  'attrs', 'components',
                  'container', 'location')

    def create(self, validated_data):
        # metadata = validated_data.pop('metadata', None)
        attrs_data = validated_data.pop('attrs')
        components_data = validated_data.pop('components')

        with transaction.atomic():
            # metadata = GenericData.objects.create(
            #     value=metadata,
            # )

            attrs = []
            for atrr_data in attrs_data:
                attr = Attribute.objects.create(**atrr_data)
                attrs.append(attr)

            validated_data.update(attrs=attrs)
            device = Device.create(**validated_data)

            for component_data in components_data:
                component_data.update(device=device)
                Component.objects.create(**component_data)

        # UPDATE METADATA COMPONENT AND DEVICE

        return device


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = ('id', 'name', 'value')

    def save(self, **kwargs):
        instance = super(AttributeSerializer, self).save()

        if 'device' in kwargs:
            kwargs.get('device').attrs.add(instance)

        return instance
