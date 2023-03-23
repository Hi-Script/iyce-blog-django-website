from django.apps import AppConfig


class IyceeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iycee'

    def ready(self):
        import iycee.signals
