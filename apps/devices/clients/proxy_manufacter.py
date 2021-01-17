# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.manufacters.interfaces.factories import ManufacterFactoryService

from iot_devices.proto.devices_pb2 import (
    Payload as PayloadProto,
    Device as DeviceProto,
    Trait as TraitProto
)
from iot_devices.proto.wrapper import PayloadWrapper


class ProxyManufacter(object):
    """
    Se encarga de manipular la data antes de enviar al service manufacter
    Ademas registro el evento.
    """

    @classmethod
    def execute_sync(cls, device):
        payload_proto = PayloadProto(
            type=PayloadProto.PayloadType.SYNC,
            sub_type=PayloadProto.PayloadSubType.PAYLOAD_SUB_TYPE_NONE,
            device=DeviceProto(  # Pass the name to update
                name=device.name
            )
        )
        ManufacterFactoryService.get_service(device.manufacter).send(
            device,
            payload_proto
        )

    @classmethod
    def execute_refresh(cls, device):
        assert device.is_ready()

        payload_proto = PayloadProto(
            type=PayloadProto.PayloadType.STATE,
            sub_type=PayloadProto.PayloadSubType.PAYLOAD_SUB_TYPE_NONE,
        )
        ManufacterFactoryService.get_service(device.manufacter).send(
            device,
            payload_proto
        )

    @classmethod
    def execute_action(cls, device, data, user=None):
        assert device.is_ready()

        default_data = data.pop('data', {})  # Get default data
        data.update(default_data)  # Join default data

        device_proto = DeviceProto()
        for key, value in data.items():
            device_proto.values[key] = str(value)

        payload_proto = PayloadProto(
            type=PayloadProto.PayloadType.EXECUTE,
            sub_type=PayloadProto.PayloadSubType.PAYLOAD_SUB_TYPE_NONE,
            device=device_proto
        )
        ManufacterFactoryService.get_service(device.manufacter).send(
            device,
            payload_proto
        )

        device.register_action(PayloadWrapper(payload_proto), user)

    @classmethod
    def execute_action_component(cls, component, data, user=None):
        assert device.is_ready()

        default_data = data.pop('data', {})  # Get default data
        data.update(default_data)  # Join default data

        payload_proto = PayloadProto(
            type=PayloadProto.PayloadType.EXECUTE,
            sub_type=PayloadProto.PayloadSubType.PAYLOAD_SUB_TYPE_NONE,
            device=DeviceProto()
        )

        trait_proto = TraitProto(
            id=component.external_id
        )
        for key, value in data.items():
            trait_proto.values[key] = str(value)
            # Append to payload
            payload_proto.traits.append(trait_proto)

        ManufacterFactoryService.get_service(component.device.manufacter).send(
            component.device,
            payload_proto
        )

        component.register_action(PayloadWrapper(payload_proto), user)
