from django.apps import AppConfig


class ShiojiaApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shiojia_api'
    def ready(self):
        from . import app_initializer