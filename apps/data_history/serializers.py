# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from apps.data_history.models import DataHistory


class DataHistorySerializer(serializers.ModelSerializer):
    status_data = serializers.SerializerMethodField()
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = DataHistory
        fields = ('id', 'status_data', 'content_type', 'object_id', 'created_at')

    def get_status_data(self, obj):
        return obj.get_status_data()

    def get_content_type(self, obj):
        return obj.content_type.name
