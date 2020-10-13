# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from google.protobuf.json_format import MessageToJson

from .devices_pb2 import Payload


class PayloadWrapper:

    def __init__(self, payload: Payload):
        self.payload = payload

    def __getattr__(self, attribute):
        if attribute not in ['payload']:
            return getattr(self.payload, attribute)
        return super().__getattr__(attribute)

    def __setattr__(self, attribute, value):
        if attribute not in ['payload']:
            return setattr(self.payload, attribute, value)
        return super().__setattr__(attribute, value)

    def to_json(self):
        return MessageToJson(
            self.payload,
            use_integers_for_enums=True
        )

    def to_dict(self):
        return json.loads(self.to_json())

# getattr(de, d.name) for d in de.DESCRIPTOR.fields
