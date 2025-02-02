from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feeds'

    def ready(self) -> None:
        from . import signals
        return super().ready()