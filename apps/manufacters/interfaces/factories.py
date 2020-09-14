# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.manufacters.constants import (
    MANU_TYPE_MQTT
)

from .mqtt.services import ManufacterMQTTService

SERVICES = {
    MANU_TYPE_MQTT: ManufacterMQTTService
}


class ManufacterFactoryService():

    @classmethod
    def get_service(cls, manufacter, **kwargs):
        if manufacter.type not in SERVICES:
            raise NotImplemented
        return SERVICES[manufacter.type](manufacter, **kwargs)
