# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters import filters, rest_framework
from django.contrib.contenttypes.models import ContentType

from apps.data_history.models import DataHistory


class DataHistoryFilter(rest_framework.FilterSet):
    content_type_name = filters.ChoiceFilter(method='filter_by_content_type', choices=[
        ('device', 'Dispositivo'), ('sensor', 'Sensor'), ('actuator', 'Actuador'),
        ('controller', 'Controlador')
    ])

    def filter_by_content_type(self, queryset, key, value, *args, **kwargs):
        ct = ContentType.objects.get(model=value)
        return queryset.filter(content_type=ct)

    class Meta:
        model = DataHistory
        fields = [
            'content_type_name', 'object_id'
        ]
