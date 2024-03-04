from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AbstractuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_customer'
    label = 'customer'
    verbose_name = _('Customers')
