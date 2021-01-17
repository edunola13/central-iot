# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.dispatch import receiver

from iot_devices.gateways.proxy import GatewayProxyService
from iot_devices.models_md import DeviceInfo

from apps.manufacters.interfaces.internal.events import send_signal


#
# DECLARE OBSERVERS
#

# Observer for internal interfaces
@receiver(send_signal)
def send(sender, **kwargs):
    """
    Recibe el evento para enviar un mensaje al device.
    Args:
        sender
        kargws: {
            'device_id' str: Es necesario pasarlo a uuid,
            'data' Payload
        }
    """

    device = DeviceInfo.get_device(uuid.UUID(kwargs['device_id']))

    # Enviar por el gateway correspondiente el mensaje
    GatewayProxyService.send(
        device,
        kwargs['data']
    )
