from django.apps import AppConfig


class ProviderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.provider'
    verbose_name = 'Поставщик'
