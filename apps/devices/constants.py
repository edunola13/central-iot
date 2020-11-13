# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

# Types refer to general behaviors, not specific devices
# Aca lo voy a ir acomodando segun las necesidades del front para que sea mas facil identificar
TYPE_OTHER = 'OTHER'
TYPE_SENSOR = 'SENSOR'
TYPE_ACTUATOR = 'ACTUATOR'

DEVICE_TYPE_CHOICES = (
    (TYPE_OTHER, _('Otro Dispositivo')),
    (TYPE_SENSOR, _('Dispositivo de Sensores')),
    (TYPE_ACTUATOR, _('Dispositivo de Actuadores')),
)

STATUS_INITIAL = 'INI'  # Se crea el device y espera una respuesta de tipo SYNC
STATUS_OK = 'OK'  # Se recibe la respuesta de tipo SYNC
STATUS_ERROR = 'ERROR'  # Se recibe la respuesta de tipo SYNC pero falla
STATUS_DISCONNECT = 'DISCO'  # A definir...
DEVICE_STATUS_CHOICES = (
    (STATUS_INITIAL, _('Configurando')),
    (STATUS_OK, _('Correcto')),
    (STATUS_ERROR, _('Error')),
    (STATUS_DISCONNECT, _('Desconectado')),
)

QUERY_NONE = 'NONE'
QUERY_SYNC = 'SYNC'
QUERY_EXECUTE = 'EXECUTE'
QUERY_STATE = 'STATE'

PROTO_TO_QUERY = {
    0: QUERY_NONE,
    1: QUERY_SYNC,
    2: QUERY_EXECUTE,
    3: QUERY_STATE
}

QUERY_SUB_TYPE_NONE = 'NONE'
QUERY_SUB_TYPE_NOTIFY = 'NOTIFY'  # Cambio de un estado
QUERY_SUB_TYPE_REPORT = 'REPORT'  # Reporte de estado constante
QUERY_SUB_TYPE_ALERT = 'ALERT'  # Cambio de un estado importante

PROTO_TO_QUERY_SUB = {
    0: QUERY_SUB_TYPE_NONE,
    1: QUERY_SUB_TYPE_NOTIFY,
    2: QUERY_SUB_TYPE_REPORT,
    3: QUERY_SUB_TYPE_ALERT
}

QUERY_SUB_TYPE_CHOICES = (
    (QUERY_SUB_TYPE_NONE, _('Ninguno')),
    (QUERY_SUB_TYPE_REPORT, _('Reporte')),
    (QUERY_SUB_TYPE_NOTIFY, _('Notificacion')),
    (QUERY_SUB_TYPE_ALERT, _('Alerta')),
)

QUERY_ACTION_TYPE_USER = 'USER'
QUERY_ACTION_TYPE_RULE = 'RULE'

QUERY_STATE_TYPE_CHOICES = (
    (QUERY_ACTION_TYPE_USER, _('Usuario')),
    (QUERY_ACTION_TYPE_RULE, _('Regla')),
)
