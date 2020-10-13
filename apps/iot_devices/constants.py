# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


MODEL_TYPE_WEATHER_STATION = 'WEA_STA_ESP'
MODEL_TYPE_RELAYS = 'RELAYS'

MODEL_TYPE_CHOICES = (
    (MODEL_TYPE_WEATHER_STATION, _('Estacion Meteorologica')),
    (MODEL_TYPE_RELAYS, _('Controladora Relays')),
)

# Supported cloud services
CLOUD_SERVICES_HIBRIS = 'HIBRIS'
CLOUD_SERVICES_GOOGLE = 'GOOGLE'
CLOUD_SERVICES_AMAZON = 'AMAZON'
