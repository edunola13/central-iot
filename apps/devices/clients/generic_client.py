# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests


class GenericDeviceClient():

    def __init__(self, base_url, access_key=''):
        self.base_url = base_url
        self.access_key = access_key

    def get_info(self):
        try:
            url = "{}/info".format(
                self.base_url
            )
            res = requests.get(url, timeout=1.5)
            return res.json()
        except:
            return None

    def get_config(self):
        try:
            url = "{}/config".format(
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
