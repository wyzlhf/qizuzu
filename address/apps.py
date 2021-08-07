from django.apps import AppConfig


class AddressConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'address'
    verbose_name = '送货地址'
    verbose_name_plural = verbose_name
