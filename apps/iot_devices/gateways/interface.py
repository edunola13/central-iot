# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.conf import settings

from google.protobuf.json_format import MessageToJson

from apps.iot_devices.proto.devices_pb2 import Payload

from apps.iot_devices.models_md import DeviceInfo

from .mqtt.interface import MQTTInterfaceService


INTERFACES = {
    'MQTT': MQTTInterfaceService,
}


class GatewayInterfaceService():
    """Gateway Interface."""

    @classmethod
    def get_interface(cls, gateway: str) -> any:
        """Return the rigth gateway."""
        return INTERFACES[gateway]

    @classmethod
    def send(cls, device: DeviceInfo, payload: Payload):
        """
        Recibe el device_id y el payload a enviar al device.

        Args:
            device (DeviceInfo): Identificador de device
            payload (Payload): Payload a enviar
        """

        payload_dict = json.loads(MessageToJson(
            payload, use_integers_for_enums=True
        ))
        cls.get_interface(device.gateway).send(
            device.device_id,
            payload_dict
        )
