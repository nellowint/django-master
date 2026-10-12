from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'apps.cars'
    verbose_name = 'Carros'

    def ready(self):
        import apps.cars.signals
