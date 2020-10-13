# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
import json

from django.conf import settings

from commons.connection.mqtt.client import ClientMqtt


class MQTTInterfaceService():

    @staticmethod
    def send(device_id: uuid.UUID, payload: dict):
        """
        Recibe el device_id y el payload a enviar al device.

        Args:
            device_id (str): Identificador unico de device
            payload (dict): Payload a enviar
        """

        connect_info = {
            'MQTT_USERNAME': settings.MQTT_USERNAME_IOT,
            'MQTT_PASSWORD': settings.MQTT_PASSWORD_IOT,
            'MQTT_HOST': settings.MQTT_HOST_IOT,
            'MQTT_PORT': settings.MQTT_PORT_IOT,
            'MQTT_KEEP_ALIVE': settings.MQTT_KEEP_ALIVE_IOT
        }

        client = ClientMqtt(connect_info)
        client.loop()

        client.publish_wait(
            'client/{}/sub'.format(str(device_id)),
            json.dumps(payload)
        )

    @staticmethod
    def receive(topic: str, payload: dict):
        """
        Recibe un topico y el payload asociado.

        Args:
            topic (str): Topico donde viene el "device_id" y "method"
            payload (dict): Payload recibido
        """
        from apps.iot_devices.clouds.proxy import ProxyClouds

        topic_splitted = topic.split("/")
        if len(topic_splitted) < 3:
            # Ignore
            return

        device_id = topic_splitted[1]
        method = topic_splitted[2]  # For now: pub, sub.

        if method == "pub":
            ProxyClouds.send_to_clouds(device_id, payload)

        if method == "sub":
            # Escucharia lo que yo mando
            pass
