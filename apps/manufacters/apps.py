from django.apps import AppConfig


class ManufactersConfig(AppConfig):
    name = 'apps.manufacters'

    def ready(self):
        import apps.manufacters.signals
