from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django_customer.admin_forms import UserChangeForm, UserCreationForm
from django_customer.models import Customer


@admin.register(Customer)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["phone_number", "email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["phone_number", "password", "is_active"]}),
        (_("Personal info"), {"fields": ["first_name", "last_name", "email", "address"]}),
        (_("Permissions"), {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["phone_number", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["phone_number"]
    ordering = ["phone_number"]
    filter_horizontal = []
