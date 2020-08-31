# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.conf import settings

from manufacters.services.interfaces import ManufacterInterfaceServices

from .client_mqtt import ClientMqtt

from apps.devices.models import Device


class ManufacterMQTTService(ManufacterInterfaceServices):

    def __init__(self, manufacter):
        self.manufacter = manufacter

    def connect(self):
        connect_info = {
            'MQTT_USERNAME': settings.MQTT_SERVERS[self.manufacter.id].get('MQTT_USERNAME', None),
            'MQTT_PASSWORD': settings.MQTT_PASSWORD,
            'MQTT_HOST': settings.MQTT_HOST,
            'MQTT_PORT': settings.MQTT_PORT,
            'MQTT_KEEP_ALIVE': settings.MQTT_KEEP_ALIVE
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
        device = Device.objects.get(external_id=client, manufacter=self.manufacter)
        #
        # For now simple, always comes SYNC
        # Options: SYNC, SYNC_PARTIAL, ACTION
        #
        device.receive_sync(payload)
