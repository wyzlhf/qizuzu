from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
    verbose_name = '用户数据'
    verbose_name_plural = verbose_name
