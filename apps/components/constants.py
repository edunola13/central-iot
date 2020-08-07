# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


# Types refer to general behaviors, not specific devices
TYPE_OTHER = 'OTHER'
TYPE_SENSOR = 'SENSOR'
TYPE_ON_OFF = 'ON_OFF'

COMPONENT_TYPE_CHOICES = (
    (TYPE_OTHER, _('Otro Componente / Comportamiento')),
    (TYPE_SENSOR, _('Estado Sensor')),
    (TYPE_ON_OFF, _('Prender / Apagar')),
)

EVENT_STATE_TYPE_REPORT = 'REPORT'  # Reporte de estado constante
EVENT_STATE_TYPE_NOTIFY = 'NOTIFY'  # Cambio de un estado
EVENT_STATE_TYPE_ALERT = 'ALERT'  # Cambio de un estado importante

EVENT_STATE_TYPE_CHOICES = (
    (EVENT_STATE_TYPE_REPORT, _('Reporte')),
    (EVENT_STATE_TYPE_NOTIFY, _('Notificacion')),
    (EVENT_STATE_TYPE_ALERT, _('Alerta')),
)

EVENT_ACTION_TYPE_USER = 'USER'
EVENT_ACTION_TYPE_RULE = 'RULE'

EVENT_STATE_TYPE_CHOICES = (
    (EVENT_ACTION_TYPE_USER, _('usuario')),
    (EVENT_ACTION_TYPE_RULE, _('Regla')),
)
