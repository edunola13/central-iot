# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.dispatch

#
# This is send by Manufacter Internal
# device_id = external_id
#
send_signal = django.dispatch.Signal(
    providing_args=["device_id", "data"]
)

#
# This is send by iot_devices
# device_id = external_id
#
receive_signal = django.dispatch.Signal(
    providing_args=["manufacter", "device_id", "payload"]
)
