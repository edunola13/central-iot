# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from ir.models import IrControl, IrAction
from django.contrib.auth.models import User

class IrControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = IrControl
        fields = ('id', 'name', 'created', 'owner',)
        read_only_fields = ('owner',)


class IrActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = IrAction
        fields = ('id', 'name', 'decodeType', 'address', 'value', 'bits', 'rawlen', 'control', 'created')