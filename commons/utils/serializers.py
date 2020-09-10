# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from django_module_common.utils.serializers import JSONField


class MetadataSerializer(serializers.Serializer):
    config_metadata = JSONField(required=False)
