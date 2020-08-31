# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class ManufacterInterfaceService():

    def send(self, device, data):
        raise NotImplemented

    def receive(self, **kwargs):
        raise NotImplemented
