# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class IrControl(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # No crea relacion inversa, ya que ponemos related_name='+'
    owner = models.ForeignKey('auth.User', related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class IrAction(models.Model):
    name = models.CharField(max_length=25)
    decode_type = models.IntegerField(default=0)
    address = models.IntegerField(default=0)
    value = models.FloatField(default=0)
    bits = models.IntegerField(default=0)
    rawlen = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    control = models.ForeignKey('IrControl', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
