# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.devices.constants import (
    DEVICE_TYPES,
    DEVICE_STATUS_CHOICES, DEVICE_STATUS_INI,
)


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
    last_connection = models.DateTimeField(null=True)
    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
