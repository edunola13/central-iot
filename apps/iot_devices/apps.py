from django.apps import AppConfig


class IOTDevicesConfig(AppConfig):
    name = 'apps.iot_devices'

    def ready(self):
        import apps.iot_devices.signals
