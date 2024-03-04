# django-customer


django-customer is a Django app implements the client model. Contains a minimum set of fields such as
phone number, email, first name, last name, address. A phone number is used instead of a username.


## Quick start

1. Install app `pip install ../django-customer/dist/django-customer-0.1.tar.gz`
   
2. Add "customer" to your INSTALLED_APPS setting like this
    ```python
   INSTALLED_APPS = [
      ...,
      "django_customer",
   ]
    ```
    
3. Add to settings.py 
   ```python
   AUTH_USER_MODEL = 'customer.Customer'
   ```
4. Run `python manage.py migrate` to create the models.

5. Execute the command `manage.py createsuperuser` and enter phone number and password

Enjoy