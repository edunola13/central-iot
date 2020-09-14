from django.apps import AppConfig


class IOTDevicesConfig(AppConfig):
    name = 'iot_devices'

   	def ready(self):
        import apps.iot_devices.signals
