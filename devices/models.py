# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Device(models.Model):
    TYPE_SENSOR = 'SENSOR'
    TYPE_ACTUATOR = 'ACTUATOR'
    DEVICE_TYPES = (
        (TYPE_SENSOR, 'Dispositivo de Sensores'),
        (TYPE_ACTUATOR, 'Dispositivo de Actuadores Simples')
    )

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=True, default='')
    deviceType = models.CharField(choices=DEVICE_TYPES, default=TYPE_SENSOR, max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    #Esta clase meta es para describir cosas especificas de la base, como ordenar, nombre de tabla, etc.
    class Meta:
        ordering = ('name',)
