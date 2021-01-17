# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.devices.models import Device
from apps.components.models import Component
from apps.locations.models import Location
from apps.manufacters.models import Manufacter
from django_module_attr.models import Attribute


class DeviceService(object):
    """
    Servicio para Devices.

    La idea es ver si aca hacemos el punto intermedio que registra los devices y otras cosas.

    POR AHORA NO LO VEO DEL TODO REQUERIDO, es muy simple el alta por lo que no la complicaria.
    Ademas ya estan los metodos create de Device y Component que obligan a respetar eso.
    """

    # def create(self, device_data: dict, components_data = [], attrs_data = []):
    #     attrs_data = validated_data.pop('attrs')
    #     components_data = validated_data.pop('components')

    #     with transaction.atomic():
    #         attrs = []
    #         for atrr_data in attrs_data:
    #             attr = Attribute.objects.create(**atrr_data)
    #             attrs.append(attr)

    #         validated_data.update(attrs=attrs)
    #         device = Device.create(**validated_data)

    #         for component_data in components_data:
    #             component_data.update(device=device)
    #             Component.create(**component_data)
