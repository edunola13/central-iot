# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import receiver

from apps.manufacters.interfaces.internal.events import send_signal
from apps.iot_devices.services.internal_interface import InternalInterfaceService


#
# DECLARE OBSERVERS
#

# Observer for internal interfaces
@receiver(send_signal)
def send(sender, **kwargs):
    services = InternalInterfaceService()
    services.send_mqtt(kwargs['device_id'], kwargs['data'])
