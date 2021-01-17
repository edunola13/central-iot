# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import binascii
import secrets

from django.utils import timezone

from django_module_common.simple_mongo_model.model import ModelBase


class DeviceInfo(ModelBase):
    _collection_name = 'devices_info'

    @classmethod
    def create(cls, device_id, model_type, version):
        device = cls.create_no_save(device_id, model_type, version)
        device.save()
        return device

    @classmethod
    def create_no_save(cls, device_id, model_type, version):
        event = cls({
            'device_id': device_id,  # ID declared in physical device
            # Serial Number???
            'model_type': model_type,
            'gateway': 'MQTT',
            'version': version,
            'secret_key': binascii.hexlify(secrets.token_bytes(10)).decode(),
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        })
        return event

    @classmethod
    def get_device(cls, device_id):
        query = DeviceInfo.get_collection().find({
            'device_id': device_id
        })
        return DeviceInfo.next_object(query)


class DeviceCloud(ModelBase):
    _collection_name = 'devices_cloud'

    @classmethod
    def create(cls, device_id, cloud):
        device = cls.create_no_save(device_id, cloud)
        device.save()
        return device

    @classmethod
    def create_no_save(cls, device_id, cloud):
        event = cls({
            'device_id': device_id,  # ID declared in physical device
            'cloud': cloud,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        })
        return event
