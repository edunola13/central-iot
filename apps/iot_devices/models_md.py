# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import binascii
import secrets

from django.utils import timezone

from django_module_common.simple_mongo_model.model import ModelBase


class DeviceInfo(ModelBase):
    _collection_name = 'devices_info'

    @classmethod
    def create(cls, device_id, type, version):
        device = cls.create_no_save(device_id, type, version)
        device.save()
        return device

    @classmethod
    def create_no_save(cls, device_id, type, version):
        event = cls({
            'device_id': device_id,  # ID declared in physical device
            # Serial Number???
            'type': type,
            # Gateway??? En base al gateway sale por determinado lado
            'version': version,
            'secret_key': binascii.hexlify(secrets.token_bytes(10)).decode(),
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        })
        return event

    @classmethod
    def get_device(cls, device_id, secret_key):
        query = DeviceInfo.get_collection().find({
            'device_id': device_id,
            'secret_key': secret_key
        })
        return DeviceInfo.next_object(query)
