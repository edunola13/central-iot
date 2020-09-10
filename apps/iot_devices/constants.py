# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


TYPE_WEATHER_STATION = 'WEA_STA_ESP'
TYPE_RELAYS = 'RELAYS'

TYPE_CHOICES = (
    (TYPE_WEATHER_STATION, _('Estacion Meteorologica')),
    (TYPE_RELAYS, _('Controladora Relays')),
)
