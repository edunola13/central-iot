# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.utils import timezone

from iot_devices.gateways.mqtt.worker_listener_mqtt import WorkerMqtt


class Command(BaseCommand):
    help = 'Start Listener/Subscription MQTT'

    def handle(self, *args, **kwargs):
        worker = WorkerMqtt()
        worker.loop_forever()
