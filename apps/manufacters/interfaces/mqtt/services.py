# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.conf import settings

from apps.manufacters.interfaces.interfaces import ManufacterInterfaceService

from apps.devices.constants import QUERY_SYNC, QUERY_STATE

from commons.connection.mqtt.client import ClientMqtt


class ManufacterMQTTService(ManufacterInterfaceService):

    def __init__(self, manufacter):
        self.manufacter = manufacter

    def connect(self):
        connect_info = {
            'MQTT_USERNAME': settings.MQTT_SERVERS_MANUFACTER,
            'MQTT_PASSWORD': settings.MQTT_PASSWORD_MANUFACTER,
            'MQTT_HOST': settings.MQTT_HOST_MANUFACTER,
            'MQTT_PORT': settings.MQTT_PORT_MANUFACTER,
            'MQTT_KEEP_ALIVE': settings.MQTT_KEEP_ALIVE_MANUFACTER
        }

        self.client = ClientMqtt(connect_info)
        self.client.loop()

    def send(self, device, data):
        self.connect()
        self.client.publish_wait(
            'client/{}/sub/'.format(device.external_id),
            json.dumps(data)
        )

    def receive(self, client, topic, payload):
        from apps.devices.models import Device

        device = Device.objects.get(external_id=client, manufacter=self.manufacter)
        if payload['type'] == QUERY_SYNC:
            device.receive_sync(payload)
        if payload['type'] == QUERY_STATE:
            device.receive_state(payload)
