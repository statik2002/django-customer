# django-customer


django-customer is a Django app implements the client model. Contains a minimum set of fields such as
phone number, email, first name, last name, address. A phone number is used instead of a username.


## Quick start
1. Download archive from [/django-customer/dist/django-customer-0.1.tar.gz](https://github.com/statik2002/django-customer/blob/master/django-customer/dist/django-customer-0.0.1a0.tar.gz)

1. Install Django `pip install Django`

2. Create Django project `django-admin startproject djangoproject`

3. Install app `pip install ../django-customer/dist/django-customer-0.1.tar.gz`
   
4. Add "customer" to your INSTALLED_APPS setting like this
    ```python
   INSTALLED_APPS = [
      ...,
      "django_customer",
   ]
    ```
    
5. Add to settings.py 
   ```python
   AUTH_USER_MODEL = 'customer.Customer'
   ```
6. Run `python manage.py migrate` to create the models.

7. Execute the command `manage.py createsuperuser` and enter phone number and password

Enjoy
