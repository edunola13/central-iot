# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import uuid

from google.protobuf.json_format import Parse

from apps.iot_devices.proto.devices_pb2 import Payload

from .hibris.base import HibrisService


class ProxyClouds(object):
    """
    Esta clase se encarga de distribuir los mensajes a los clouds
    correspondientes segun corresponda para un device.
    """

    def __init__(self, arg):
        pass

    @classmethod
    def send_to_clouds(cls, device_id, payload: str):
        """
        For now only send to Hibris
        The device can have many clouds associated
        """

        device_id = uuid.UUID(device_id)

        payload_proto = Payload()
        Parse(
            payload,
            payload_proto,
            ignore_unknown_fields=False
        )

        hibris = HibrisService(device_id)
        hibris.send_to_cloud(payload_proto)
