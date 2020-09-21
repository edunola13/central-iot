# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.manufacters.interfaces.interfaces import ManufacterInterfaceService

from apps.devices.constants import RECEIVE_SYNC, RECEIVE_STATE

from apps.devices.models import Device

from .events import send_signal


class ManufacterInternalService(ManufacterInterfaceService):

    def __init__(self, manufacter):
        self.manufacter = manufacter

    def send(self, device, data):
        # Este envia a iot_devices el cual conoce y respeta el formato
        send_signal.send(
            sender=self.__class__,
            device_id=device.external_id,
            data=data
        )

    def receive(self, device_id, payload):
        # Este recibe desde iot_devices el cual conoce y respeta el formato
        device = Device.objects.get(external_id=device_id, manufacter=self.manufacter)
        if payload['type'] == RECEIVE_SYNC:
            device.receive_sync(payload)
        if payload['type'] == RECEIVE_STATE:
            device.receive_state(payload)
