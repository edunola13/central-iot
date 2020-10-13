# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import receiver

from apps.manufacters.interfaces.internal.events import receive_signal
from apps.manufacters.interfaces.internal.services import ManufacterInternalService

from apps.manufacters.models import Manufacter


#
# DECLARE OBSERVERS
#
@receiver(receive_signal)
def receive(sender, **kwargs):
    services = ManufacterInternalService(
        manufacter=Manufacter.objects.get(manu_uuid=kwargs['manufacter_uuid'])
    )
    services.receive(kwargs['device_id'], kwargs['data'])
