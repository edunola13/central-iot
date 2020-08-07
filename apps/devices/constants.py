# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


# Types refer to general behaviors, not specific devices
TYPE_OTHER = 'OTHER'
TYPE_SENSOR = 'SENSOR'
TYPE_ACTUATOR = 'ACTUATOR'

DEVICE_TYPE_CHOICES = (
    (TYPE_OTHER, _('Otro Dispositivo')),
    (TYPE_SENSOR, _('Dispositivo de Sensores')),
    (TYPE_ACTUATOR, _('Dispositivo de Actuadores')),
)

STATUS_INITIAL = 'INI'
STATUS_OK = 'OK'
STATUS_ERROR = 'ERROR'
STATUS_DISCONNECT = 'DISCO'
DEVICE_STATUS_CHOICES = (
    (STATUS_INITIAL, _('Configurando')),
    (STATUS_OK, _('Correcto')),
    (STATUS_ERROR, _('Error')),
    (STATUS_DISCONNECT, _('Desconectado')),
)
