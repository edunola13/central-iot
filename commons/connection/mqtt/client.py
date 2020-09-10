# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

import paho.mqtt.client as mqtt

from paho.mqtt.client import MQTT_ERR_SUCCESS


class ClientMqtt(object):

    def __init__(self, connect_info):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.connected = False
        self.connected_error = False

        self.client.username_pw_set(connect_info['MQTT_USERNAME'], connect_info['MQTT_PASSWORD'])
        self.client.connect(connect_info['MQTT_HOST'], connect_info['MQTT_PORT'], connect_info['MQTT_KEEP_ALIVE'])

    def loop(self):
        self.client.loop()

    def loop_start(self):
        # This is part of the threaded client interface. Call this once to
        # start a new thread to process network traffic. This provides an
        # alternative to repeatedly calling loop() yourself
        # - loop(): Lo llamamos a mano para ver si hay mensajes.
        self.client.loop_start()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        logging.info("Connected with result code: {}".format(rc))
        if rc == MQTT_ERR_SUCCESS:
            self.connected = True
        else:
            self.connected = False
            self.connected_error = True

    def on_disconnect(self, client, userdata, rc):
        logging.info("Disconnected from the broker")
        self.connected = False
        self.connected_error = False

    def publish(self, topic, data):
        info = self.client.publish(topic, data)
        return info

    def publish_wait(self, topic, data):
        info = self.client.publish(topic, data)
        if info.rc != MQTT_ERR_SUCCESS:
            return info
        info.wait_for_publish()
        return info
