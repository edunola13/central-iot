# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.db import models

from apps.components.constants import (
    COMPONENT_TYPES, SENSOR_TYPES, ACTUATOR_TYPES, CONTROLLER_TYPES
)


class Component(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    external_id = models.CharField(max_length=20)
    component_type = models.CharField(choices=COMPONENT_TYPES, max_length=10)
    status_data = models.TextField(max_length=500)
    record_history = models.BooleanField(default=False)
    record_interval = models.PositiveIntegerField(default=0)  # In minutes, if 0 every time the device send
    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    device = models.ForeignKey('devices.Device', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        abstract = True

    def get_status_data(self):
        try:
            return json.loads(self.status_data)
        except Exception:
            return None


class Sensor(Component):
    sensor_type = models.CharField(choices=SENSOR_TYPES, max_length=10)


class Actuator(Component):
    actuator_type = models.CharField(choices=ACTUATOR_TYPES, max_length=10)


class Controller(Component):
    controller_type = models.CharField(choices=CONTROLLER_TYPES, max_length=10)
