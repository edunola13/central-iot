# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class DataHistory(models.Model):
    status_data = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    object_related = GenericForeignKey('content_type', 'object_id')

    def get_status_data(self):
        try:
            return json.loads(self.status_data)
        except Exception:
            return None
