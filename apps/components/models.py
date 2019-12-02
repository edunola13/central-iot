# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.db import models

from apps.components.constants import (
    COMPONENT_TYPES, TYPE_SENSOR, TYPE_ACTUATOR, TYPE_CONTROLLER,
    SENSOR_TYPES, ACTUATOR_TYPES, CONTROLLER_TYPES
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

    def update_component(self, data):
        if data.get('start', False):
            self.enabled = True
            self.set_status_data(data)
        else:
            self.enabled = False
        self.save()

    def set_status_data(self, data):
        try:
            self.status_data = json.dumps(data)
            self.save()
        except Exception:
            return None

    def get_status_data(self):
        try:
            return json.loads(self.status_data)
        except Exception:
            return None


class Sensor(Component):
    sensor_type = models.CharField(choices=SENSOR_TYPES, max_length=10)

    @classmethod
    def create(cls, name, external_id, sensor_type, all_data, device):
        sensor = Sensor.objects.create(
            name=name,
            component_type=TYPE_SENSOR,
            sensor_type=sensor_type,
            external_id=external_id,
            device=device,
            enabled=all_data.get('start', False)
        )

        if sensor.enabled:
            sensor.set_status_data(all_data)

        return sensor


class Actuator(Component):
    actuator_type = models.CharField(choices=ACTUATOR_TYPES, max_length=10)

    @classmethod
    def create(cls, name, external_id, actuator_type, all_data, device):
        actuator = Actuator.objects.create(
            name=name,
            component_type=TYPE_ACTUATOR,
            actuator_type=actuator_type,
            external_id=external_id,
            status_data=json.dumps(all_data),
            device=device,
            enabled=all_data.get('start', False)
        )

        if actuator.enabled:
            actuator.set_status_data(all_data)

        return actuator


class Controller(Component):
    controller_type = models.CharField(choices=CONTROLLER_TYPES, max_length=10)

    @classmethod
    def create(cls, name, external_id, controller_type, all_data, device):
        controller = Controller.objects.create(
            name=name,
            component_type=TYPE_CONTROLLER,
            controller_type=controller_type,
            external_id=external_id,
            status_data=json.dumps(all_data),
            device=device,
            enabled=all_data.get('start', False)
        )

        if controller.enabled:
            controller.set_status_data(all_data)

        return controller
