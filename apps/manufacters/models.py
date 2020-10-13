# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models

from .constants import (
    MANU_TYPE_CHOICES,
    MANU_TYPE_INTERNAL, MANU_TYPE_MQTT, MANU_TYPE_REST
)

from django_module_attr.models import GenericData


class Manufacter (models.Model):
    MANU_TYPE_INTERNAL = MANU_TYPE_INTERNAL
    MANU_TYPE_MQTT = MANU_TYPE_MQTT
    MANU_TYPE_REST = MANU_TYPE_REST

    manu_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    type = models.CharField(max_length=10,  # Define the communication with the cloud manufacter
                            default=MANU_TYPE_INTERNAL,
                            choices=MANU_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    config = models.ForeignKey(GenericData,
                               null=True,
                               related_name="+",
                               on_delete=models.CASCADE)

    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
