# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.manufacters.interfaces.factories import ManufacterFactoryService

from apps.devices.constants import (
    QUERY_SYNC, QUERY_ACTION
)


#
# Se encarga de manipular la data antes de enviar al service manufacter
# Ademas registro el evento
#
class ProxyManufacter(object):

    @classmethod
    def execute_sync(cls, device):
        data = {'type': QUERY_SYNC}
        ManufacterFactoryService.get_service(device.manufacter).send(device, data)

    @classmethod
    def execute_action(cls, device, data, user=None):
        data.append({
            'type': QUERY_ACTION,
            'trait': None,
            # More metadata???
        })
        ManufacterFactoryService.get_service(device.manufacter).send(device, data)

        device.register_action(data, user)

    @classmethod
    def execute_action_component(cls, component, data, user=None):
        data.append({
            'type': QUERY_ACTION,
            'trait': component.id,
            # More metadata???
        })
        ManufacterFactoryService.get_service(component.device.manufacter).send(component.device, data)

        component.register_action(data, user)
