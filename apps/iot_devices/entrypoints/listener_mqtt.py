# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def main():
    from apps.iot_devices.gateways.mqtt.worker_listener_mqtt import WorkerMqtt

    worker = WorkerMqtt()
    worker.loop_forever()
