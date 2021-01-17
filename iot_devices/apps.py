from django.apps import AppConfig


class IOTDevicesConfig(AppConfig):
    name = 'iot_devices'

    def ready(self):
        import iot_devices.signals
