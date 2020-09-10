# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext as _
from django.conf import settings
from django.db import transaction

import apps.devices.constants as device_cons
import apps.components.constants as component_cons
from apps.iot_devices.constants import (
    TYPE_WEATHER_STATION, TYPE_RELAYS
)

from apps.manufacters.models import Manufacter
from apps.devices.models import Device
from apps.components.models import Component
from apps.locations.models import UserLocation

from apps.iot_devices.models_md import DeviceInfo


class RegisterDevice():

    def _get_strategy(self, type):
        if type not in STRATEGY_BY_TYPE:
            raise InvalidDeviceType

        return STRATEGY_BY_TYPE[type]()

    def _validate_device(self, device_id, secret_key):
        try:
            return DeviceInfo.get_device(device_id, secret_key)
        except:
            raise InvalidDeviceAccess

    def register(self, data, user):
        # Default data:
        # 'device_id' => 'id in the physic device', 'type', 'version', 'secret_key' => 'in the physic device'
        # 'name' => 'a label', 'location' => 'location to register(need access)'

        # Validate hte access to the device
        self._validate_device(data.get('device_id'), data.get('secret_key'))

        # Validate location with user
        has_access = UserLocation.objects.filter(
            location=data.get('location'),
            user=user,
            access__in=[UserLocation.ACCESS_OWNER, UserLocation.ACCESS_ADMIN]
        ).exists()
        if not has_access:
            raise InvalidLocation

        # Create the device with strategy
        return self._get_strategy(data.get('type')).register(data)

    def unregister(self, data):
        # Validate hte access to the device
        self._validate_device(data.get('device_id'), data.get('secret_key'))

        # Unregister
        manufacter = Manufacter.objects.get(manu_uuid=settings.INTERNAL_MANUFACTER)
        device = Device.objects.get(
            external_id=data.get('device_id'),
            manufacter=manufacter
        )

        device.remove()


#
# Strategy by device type
#
class InterfaceRegisterStrategy():

    def register(self, data, user):
        raise NotImplemented


class WeatherStationRegister():

    def register(self, data):
        with transaction.atomic():
            device = Device.create(
                external_id=data.get('device_id'),
                name=data.get('name'),
                location=data.get('location'),
                manufacter=Manufacter.objects.get(manu_uuid=settings.INTERNAL_MANUFACTER),
                type=device_cons.TYPE_SENSOR,
                config_metadata={
                    'type': data.get('type'),
                    'version': data.get('version')
                },
                container=None,
                attrs=[]
            )

            Component.create(
                external_id="1",  # It's a unique component, so is not soo important
                name=_("Medicion"),
                device=device,
                type=component_cons.TYPE_SENSOR,
                config_metadata=None,
                tags=[]
            )

        return device


class RelaysRegister():

    def register(self, data):
        # extra data = 'relays'

        with transaction.atomic():
            device = Device.create(
                external_id=data.get('device_id'),
                name=data.get('name'),
                location=data.get('location'),
                manufacter=Manufacter.objects.get(manu_uuid=settings.INTERNAL_MANUFACTER),
                type=device_cons.TYPE_ACTUATOR,
                config_metadata={
                    'type': data.get('type'),
                    'version': data.get('version')
                },
                container=None,
                attrs=[]
            )

            for i in range(1, data.get('relays', 1) + 1):
                Component.create(
                    external_id=i,
                    name=_("Relay") + ' {}'.format(i),
                    device=device,
                    type=component_cons.TYPE_ON_OFF,
                    config_metadata=None,
                    tags=[]
                )

        return device


STRATEGY_BY_TYPE = {
    TYPE_WEATHER_STATION: WeatherStationRegister,
    TYPE_RELAYS: RelaysRegister
}


#
# Exceptions
#
class InvalidDeviceAccess(Exception):
    pass


class InvalidDeviceType(Exception):
    pass


class InvalidLocation(Exception):
    pass
