# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class ManufacterInterfaceService():

    def send(self, device, data):
        raise NotImplementedError

    def receive(self, **kwargs):
        raise NotImplementedError
