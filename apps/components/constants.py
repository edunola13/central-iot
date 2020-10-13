# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


# Types refer to general behaviors, not specific devices
# Aca lo voy a ir acomodando segun las necesidades del front para que sea mas facil identificar
TYPE_OTHER = 'OTHER'
TYPE_SENSOR = 'SENSOR'  # Permite recibir informacion
TYPE_ON_OFF = 'ON_OFF'  # Permite prender/apagar determinada caracteristica
TYPE_SETTING = 'SETTING'  # Permite configurar una caracteristica

COMPONENT_TYPE_CHOICES = (
    (TYPE_OTHER, _('Otro Componente / Comportamiento')),
    (TYPE_SENSOR, _('Estado Sensor')),
    (TYPE_ON_OFF, _('Prender / Apagar')),
    (TYPE_SETTING, _('Configuracion')),
)
