# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.utils.translation import gettext as _
from django.conf import settings
from django.db import transaction

from google.protobuf.json_format import Parse
from iot_devices.proto.devices_pb2 import (
    Payload as PayloadProto,
    Device as DeviceProto
)

import apps.devices.constants as device_cons
import apps.components.constants as component_cons
from iot_devices.constants import (
    MODEL_TYPE_WEATHER_STATION, MODEL_TYPE_RELAYS
)

from apps.manufacters.models import Manufacter
from apps.devices.models import Device
from apps.components.models import Component
from apps.locations.models import UserLocation

from iot_devices.models_md import DeviceInfo

from iot_devices.gateways.proxy import GatewayProxyService
from apps.manufacters.interfaces.internal.events import receive_signal


class HibrisService():

    def __init__(self, device_id: uuid.UUID):
        try:
            self.device = DeviceInfo.get_device(device_id)
        except:
            raise DeviceDoesNotExist
        self.strategy = self._get_strategy()

    def _get_strategy(self):
        if self.device.model_type not in STRATEGY_BY_TYPE:
            raise InvalidDeviceType

        return STRATEGY_BY_TYPE[self.device.model_type](self.device)

    def _validate_device(self, secret_key: str):
        if self.device.secret_key != secret_key:
            raise InvalidDeviceAccess

    def register(self, data: dict, user):
        """
        Registra el dispositivo contra el cloud de Hibris.
        Se valida el permiso a traves de la secret_key.
        Args:
            data (dict): {
                'model_type', 'version', 'secret_key', 'name', 'location'
            }
            user (User)
        """

        # Validate the access to the device
        self._validate_device(data.get('secret_key'))

        # Validate location with user
        #
        #
        # Lo podria hacer el mismo servicio que llama el strategy
        #
        #
        has_access = UserLocation.objects.filter(
            location=data.get('location'),
            user=user,
            access__in=[UserLocation.ACCESS_OWNER, UserLocation.ACCESS_ADMIN]
        ).exists()
        if not has_access:
            raise InvalidLocation

        # Create the device with strategy
        # Every strategy know how create the basic configuration
        device = self.strategy.register(data)

        # Send sync
        payload_proto = PayloadProto(
            type=PayloadProto.PayloadType.SYNC,
            sub_type=PayloadProto.PayloadSubType.PAYLOAD_SUB_TYPE_NONE,
            device=DeviceProto(
                name=device.name
            )
        )
        GatewayProxyService.send(
            self.device,
            payload_proto
        )

        return device

    def unregister(self, data: dict):
        # Validate the access to the device
        self._validate_device(data.get('secret_key'))

        manufacter = Manufacter.objects.get(
            manu_uuid=settings.HIBRIS_MANUFACTER
        )
        device = Device.objects.get(
            external_id=self.device.device_id,
            manufacter=manufacter
        )
        device.remove()

        #
        # Unregister in model DeviceCloud
        #

    def send_to_cloud(self, payload: PayloadProto):
        """
        Recibe el payload enviado por el device.

        Args:
            payload PayloadProto
        """

        receive_signal.send(
            sender=self.__class__,
            manufacter_uuid=settings.HIBRIS_MANUFACTER,
            device_id=self.device.device_id,
            data=payload
        )

#
# Strategy by device type
#
class BaseHibrisStrategy():

    def __init__(self, device):
        self.device = device

    def register(self, data, user):
        raise NotImplementedError


class WeatherStationStrategy(BaseHibrisStrategy):

    def register(self, data: dict):
        with transaction.atomic():
            device = Device.create(
                external_id=self.device.device_id,
                name=data.get('name'),
                location=data.get('location'),
                manufacter=Manufacter.objects.get(manu_uuid=settings.HIBRIS_MANUFACTER),
                type=device_cons.TYPE_SENSOR,
                config_metadata={
                    'type': MODEL_TYPE_WEATHER_STATION,
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


class RelaysStrategy(BaseHibrisStrategy):

    def register(self, data):
        """ extra data = 'relays' """

        with transaction.atomic():
            device = Device.create(
                external_id=self.device.device_id,
                name=data.get('name'),
                location=data.get('location'),
                manufacter=Manufacter.objects.get(manu_uuid=settings.HIBRIS_MANUFACTER),
                type=device_cons.TYPE_ACTUATOR,
                config_metadata={
                    'type': MODEL_TYPE_RELAYS,
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
    MODEL_TYPE_WEATHER_STATION: WeatherStationStrategy,
    MODEL_TYPE_RELAYS: RelaysStrategy
}


#
# Exceptions
#
class DeviceDoesNotExist(Exception):
    pass


class InvalidDeviceAccess(Exception):
    pass


class InvalidDeviceType(Exception):
    pass


class InvalidLocation(Exception):
    pass
