# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.conf import settings
from django.dispatch import receiver

from manufacters.services.interfaces import ManufacterInterfaceServices

from commons.connection.mqtt.client import ClientMqtt

from apps.manufacters.services.internal.events import send_signal, receive_signal


@receiver(send_signal)
def send(sender, **kwargs):
    services = ManufacterInternalService()
    services.send_mqtt(kwargs['device_id'], kwargs['data'])


#
# This services know how send and receive from physic devices
# Strategies could be added by type
#
class ManufacterInternalService(ManufacterInterfaceServices):

    def send_mqtt(self, device_id, data):
        #
        # ACOMODAR DE DONDE LEVANTO LAS SETTINGS
        #
        connect_info = {
            'MQTT_USERNAME': settings.MQTT_SERVERS[self.manufacter.id].get('MQTT_USERNAME', None),
            'MQTT_PASSWORD': settings.MQTT_PASSWORD,
            'MQTT_HOST': settings.MQTT_HOST,
            'MQTT_PORT': settings.MQTT_PORT,
            'MQTT_KEEP_ALIVE': settings.MQTT_KEEP_ALIVE
        }

        self.client = ClientMqtt(connect_info)
        self.client.loop()

        self.client.publish_wait(
            'client/{}/sub/'.format(device_id),
            json.dumps(data)
        )

    def receive_mqtt(self, device_id, topic, payload):
        receive_signal.send(
            sender=self.__class__,
            manufacter_id=settings.INTERNAL_MANUFACTER,
            device_id=device_id,
            data=payload
        )
