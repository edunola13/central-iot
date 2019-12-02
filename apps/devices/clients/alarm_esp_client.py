# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from apps.devices.clients.generic_client import GenericDeviceClient


class AlarmESPClient(GenericDeviceClient):

    def get_alarm_status(self):
        try:
            url = "{}/alarm".format(
                self.base_url
            )
            res = requests.get(
                url,
                headers={
                    'key': self.access_key,
                    "Content-type": "application/json"
                },
                timeout=5
            )
            return res.json()
        except:
            return None

    def get_sensors(self):
        try:
            url = "{}/sensors".format(
                self.base_url
            )
            res = requests.get(
                url,
                headers={
                    'key': self.access_key,
                    "Content-type": "application/json"
                },
                timeout=5
            )
            return res.json()
        except:
            return None
