# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from django_module_common.utils.filters import MongoFilter


class EventStateFilter(MongoFilter):
    device = serializers.UUIDField(required=False)
    component = serializers.UUIDField(required=False)
    type = serializers.CharField(required=False)
    created_at_gte = serializers.DateTimeField(required=False)
    created_at_lte = serializers.DateTimeField(required=False)

    def validate_tags(self, value):
        return [int(v) for v in value.split(",")]

    def validate(self, data):
        if 'created_at_gte' in data or 'created_at_lte' in data:
            created_at = {
                '$gte': data.pop('created_at_gte', None),
                '$lte': data.pop('created_at_lte', None)
            }
            data['created_at'] = {k: v for k, v in created_at.items() if v is not None}

        return data


class EventActionFilter(MongoFilter):
    device = serializers.UUIDField(required=False)
    component = serializers.UUIDField(required=False)
    type = serializers.CharField(required=False)
    created_at_gte = serializers.DateTimeField(required=False)
    created_at_lte = serializers.DateTimeField(required=False)

    def validate_tags(self, value):
        return [int(v) for v in value.split(",")]

    def validate(self, data):
        if 'created_at_gte' in data or 'created_at_lte' in data:
            created_at = {
                '$gte': data.pop('created_at_gte', None),
                '$lte': data.pop('created_at_lte', None)
            }
            data['created_at'] = {k: v for k, v in created_at.items() if v is not None}

        return data
