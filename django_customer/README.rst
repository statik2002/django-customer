============
django-customer
============

django-customer is a Django app implements the client model. Contains a minimum set of fields such as
phone number, email, first name, last name, address. A phone number is used instead of a username.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "customer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_customer",
    ]


2. Run ``python manage.py migrate`` to create the models.

3. Execute the command ``manage.py createsuperuser`` and enter phone number and password
