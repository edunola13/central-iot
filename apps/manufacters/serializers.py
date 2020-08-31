# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction

from rest_framework import serializers

from django_module_common.utils.serializers import JSONField

from .models import Manufacter
from django_module_attr.models import GenericData


class ManufacterMinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacter
        fields = ('id', 'manu_uuid', 'name', 'type',
                  'enabled', 'created_at', 'updated_at')


class AdminManufacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacter
        fields = ('id', 'manu_uuid', 'name', 'type',
                  'enabled', 'created_at', 'updated_at')
        read_only_fields = (
            'id', 'manu_uuid', 'status',
            'created_at', 'updated_at')


class ManufacterCreateSerializer(serializers.ModelSerializer):
    config = JSONField(required=False)

    class Meta:
        model = Manufacter
        fields = ('name', 'type',
                  'config', 'enabled',)

    def create(self, validated_data):
        config_value = validated_data.pop('config', None)

        with transaction.atomic():
            config = None
            if config_value:
                config = GenericData.objects.create(value=config_value)

            instance = super(ManufacterCreateSerializer, self).create(validated_data)
            instance.config = config
            instance.save()

        return instance


class AdminConfigSerializer(serializers.ModelSerializer):
    value = JSONField()

    class Meta:
        model = GenericData
        fields = ('id', 'value')

    def save(self, **kwargs):
        manufacter = kwargs.get('manufacter')
        instance = super(AdminConfigSerializer, self).save()
        if manufacter.config is None:
            manufacter.config = instance
            manufacter.save()

        return instance
