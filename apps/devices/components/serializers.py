# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction

from rest_framework import serializers

from django_module_common.utils.serializers import JSONField

from apps.components.models import Component
from django_module_attr.models import Tag

from django_module_attr.serializers import TagSerializer


class ComponentSerializer(serializers.ModelSerializer):
    metadata = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Component
        fields = ('id', 'external_id', 'name', 'type',
                  'metadata', 'tags', 'device',
                  'enabled', 'created_at', 'updated_at')
        read_only_fields = ('id', 'metadata', 'device',
                            'created_at', 'updated_at')

    def get_metadata(self, obj):
        if obj.metadata:
            return obj.metadata.get_value()

        return None

    def update(self, instance, validated_data):
        super(ComponentSerializer, self).update(instance, validated_data)

        # UPDATE METADATA COMPONENT AND DEVICE
        # Por ahora no haria nada

        return instance


class ComponentCreateSerializer(serializers.ModelSerializer):
    config_metadata = JSONField(required=False)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        write_only=True, many=True, required=False
    )

    class Meta:
        model = Component
        fields = ('external_id', 'name', 'type',
                  'tags', 'enabled')

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])

        with transaction.atomic():
            validated_data.update(tags=tags)
            component = Component.create(**validated_data)

        return component
