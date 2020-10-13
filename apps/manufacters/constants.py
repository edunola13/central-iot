# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

MANU_TYPE_INTERNAL = "INTERNAL"
MANU_TYPE_MQTT = "MQTT"
MANU_TYPE_REST = "REST"

MANU_TYPE_CHOICES = (
    (MANU_TYPE_INTERNAL, _('INTERNAL')),
    (MANU_TYPE_MQTT, _('MQTT')),
    (MANU_TYPE_REST, _('API REST')),
)
