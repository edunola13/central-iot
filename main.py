# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import django
import sys

from apps.iot_devices.entrypoints.listener_mqtt import main as main_iot_listener_mqtt

commands = {
    'iot_listener_mqtt': main_iot_listener_mqtt,
}


def execute_from_command_line(args):
    key = args[1]
    commands[key]()


if __name__ == '__main__':
    # Armar punto de entrada que levante los diferentes workers
    os.environ["DJANGO_SETTINGS_MODULE"] = "hibris_iot.settings"
    django.setup()
    execute_from_command_line(sys.argv)
