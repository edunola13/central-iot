# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from apps.ir.models import IrControl, IrAction


class IrControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = IrControl
        fields = ('id', 'name', 'created_at', 'updated_at', 'owner',)
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')


class IrActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = IrAction
        fields = ('id', 'name',
                  'decode_type', 'address', 'value', 'bits', 'rawlen',
                  'control', 'created_at', 'updated_at')
