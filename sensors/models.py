# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Sensor(models.Model):
    SENSOR_TYPES = (
        ('HUM_TEMP', 'Humedad - Temperatura'),
        ('GP_2', 'Sensor de Gas')
    )

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=True, default='')
    sensorType = models.CharField(choices=SENSOR_TYPES, max_length=10)
    lastRead = models.TextField(max_length=500, null=True)
    lastUpdate = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    device = models.ForeignKey('devices.Device', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class SensorReading(models.Model):
    read = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)