from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class CustomerManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number,  password=None, **extra_fields):
        user = self.create_user(phone_number, password=password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    username = None
    first_name = models.CharField(max_length=256, null=True, blank=True, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=256, null=True, blank=True, verbose_name=_('Last Name'))
    phone_number = PhoneNumberField(unique=True, verbose_name=_('Phone number'))
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('Address'))
    is_active = models.BooleanField(_('is_active'), default=True)
    is_admin = models.BooleanField(default=False, verbose_name=_('is_admin'))
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    date_joined = models.DateTimeField(
        _('Registration Date'),
        default=timezone.now
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email'

    objects = CustomerManager()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} : {self.phone_number}'

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
