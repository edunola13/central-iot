# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
# import ssl

from django.conf import settings
import paho.mqtt.client as mqtt

from apps.iot_devices.services.internal_interface import InternalInterfaceService


class WorkerMqtt(object):

    def __init__(self):
        self.client = mqtt.Client(client_id="")  # Automatic client_id
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

        self.client.message_callback_add("client/#", self.on_event)
        self.client.on_message = self.on_event_system  # For default

        self.client.username_pw_set(settings.MQTT_USERNAME_IOT, settings.MQTT_PASSWORD_IOT)
        # self.client.tls_set("/home/eduardo/Documents/mosquitto-ssl-cert/mosq-ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
        self.client.connect(settings.MQTT_HOST_IOT, settings.MQTT_PORT_IOT, settings.MQTT_KEEP_ALIVE_IOT)

        self.interface = InternalInterfaceService()

    def loop_forever(self):
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface:
        # - loop(): Lo llamamos a mano para ver si hay mensajes
        # - loop_forever(): Llama infinitamente a loop(). Maneja reconexion.
        # - loop_start(): Arranca un thread que no bloquea el hilo principal, esta bueno si hay
        # que hacer algo o hay que manejar varias conexiones. El thread por abajo hace loop_forever.
        self.client.loop_forever()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        if rc > 0:
            logging.error("Connected with result code: {}".format(rc))
            return

        logging.info("Connected with result code: {}".format(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("client/#")  # "#" is wild card
        # client.subscribe("$SYS/#")  # System events

    # The callback for when the client disconnect from the server.
    def on_disconnect(self, client, userdata, rc):
        logging.error("Disconnected with result code: {}".format(rc))

    # The callback for when a PUBLISH message is received from the server.
    def on_event_system(self, client, userdata, msg):
        # Only loggear
        logging.info("New Event System {}: {}".format(msg.topic, msg.payload))

    def on_event(self, client, userdata, msg):
        # Pasar al servicio que se encarga
        #
        # Aca se podria usar workers de zeromq del tipo pull asi se hace todo mas rapido
        #
        logging.info("New Event {}: {}: {}".format(client, msg.topic, msg.payload))
        try:
            self.interface.receive_mqtt(msg.topic, msg.payload)
        except:
            logging.exception("[MQTT IOT on_event]")
