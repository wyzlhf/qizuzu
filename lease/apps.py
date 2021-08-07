from django.apps import AppConfig


class LeaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lease'
    verbose_name = '租赁业务'
    verbose_name_plural = verbose_name
