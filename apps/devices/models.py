# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from datetime import datetime

from django.db import models

from apps.devices.constants import *
from apps.components.constants import NUMBER_TO_SENSOR_TYPE

from apps.components.models import Sensor

from apps.devices.clients import CLIENT_OF_DEVICE
from apps.devices.clients.generic_client import GenericDeviceClient


class Device(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    device_id = models.CharField(max_length=50)
    device_type = models.CharField(choices=DEVICE_TYPES, max_length=15)
    version = models.PositiveIntegerField(default=1)

    address = models.CharField(max_length=40, null=True)
    status = models.CharField(
        max_length=10,
        choices=DEVICE_STATUS_CHOICES,
        default=DEVICE_STATUS_INI)
    access_key = models.CharField(max_length=40, null=True, default='')
    status_data = models.TextField(max_length=500)
    last_connection = models.DateTimeField(null=True)
    record_history = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    _strategy = None

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    @classmethod
    def add_device_from_network(cls, network, device_type):
        network = network.split('.')
        for i in range(1, 255):
            network[3] = str(i)
            client = GenericDeviceClient('http://{}'.format('.'.join(network)))
            rta = client.get_info()

            if rta is None:
                continue

            if rta['type'] != device_type:
                continue

            device = Device.objects.filter(
                device_id=rta.get('uniqueId'),
                device_type=device_type
            ).last()
            if device is not None:
                return device

            device = Device.objects.create(
                name=rta.get('name', 'Device'),
                device_id=rta.get('uniqueId', '#1'),
                device_type=device_type,
                version=rta.get('version', 1),

                address='.'.join(network)
            )

            try:
                self._create_components()
            except:
                pass

            return device

    def _create_components(self):
        self._get_strategy().create_components()

    def get_status_data(self):
        try:
            return json.loads(self.status_data)
        except Exception:
            return None

    def _get_strategy(self):
        if not self._strategy:
            self._strategy = STRATEGY_OF_DEVICE[self.device_type](self)
        return self._strategy

    def refresh_status_data(self):
        data = self._get_strategy().get_status()
        if data:
            self.status_data = json.dumps(data)
            self.last_connection = datetime.now()
            self.save()

    def refresh_components(self):
        self._get_strategy().refresh_components()


class DeviceStrategy():

    def __init__(self, device):
        self.device = device
        self.client = CLIENT_OF_DEVICE[self.device.device_type](
            'http://{}'.format(self.device.address),
            self.device.access_key
        )

    def get_client(self):
        return CLIENT_OF_DEVICE[self.device.device_type]

    def create_components(self):
        raise NotImplementedError

    def refresh_components(self):
        raise NotImplementedError


class AlarmEspStrategy(DeviceStrategy):

    def get_status(self):
        return self.client.get_alarm_status()

    def create_components(self):
        sensors = self.client.get_sensors()
        if sensors is None:
            raise Exception("Fallo obteniendo sensores")

        for sensor in sensors:
            Sensor.create(
                'Sensor {}'.format(sensor.get('id', 0)),
                sensor.get('id', 0),
                NUMBER_TO_SENSOR_TYPE.get(sensor.get('type', 0), 'NONE'),
                sensor,
                self.device
            )

    def refresh_components(self):
        sensors = self.client.get_sensors()
        if sensors is None:
            return

        for sensor in sensors:
            try:
                sensor_obj = Sensor.objects.get(
                    external_id=sensor.get('id', 0),
                    sensor_type=NUMBER_TO_SENSOR_TYPE.get(sensor.get('type', 0), 'NONE'),
                    device=self.device
                )
                sensor_obj.update_component(sensor)
            except Sensor.DoesNotExist:
                Sensor.create(
                    'Sensor {}'.format(sensor.get('id', 0)),
                    sensor.get('id', 0),
                    NUMBER_TO_SENSOR_TYPE.get(sensor.get('type', 0), 'NONE'),
                    sensor,
                    self.device
                )


STRATEGY_OF_DEVICE = {
    TYPE_ALARM: AlarmEspStrategy
}
