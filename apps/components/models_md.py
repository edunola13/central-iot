# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from django_module_common.simple_mongo_model.model import ModelBase


class EventState(ModelBase):
    _collection_name = 'event_state'

    @classmethod
    def create(cls, device, component, type, payload):
        event = cls.create_no_save(device, component, type, payload)
        event.save()
        return event

    @classmethod
    def create_no_save(cls, device, component, type, payload):
        event = cls({
            'device': device,
            'component': component,
            'type': type,
            'payload': payload,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        })
        return event


class EventAction(ModelBase):
    _collection_name = 'event_action'

    @classmethod
    def create(cls, device, component, type, payload, user=None):
        event = cls.create_no_save(device, component, type, payload, user)
        event.save()
        return event

    @classmethod
    def create_no_save(cls, device, component, type, payload, user=None):
        event = cls({
            'device': device,
            'component': component,
            'type': type,
            'payload': payload,
            'user': user,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        })
        return event
