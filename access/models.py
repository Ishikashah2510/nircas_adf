from django.db import models

# Create your models here.


class Users(models.Model):
    user_types = [
        ('Customer', 'Customer'),
        ('Cashier', 'Cashier'),
        ('Manager', 'Manager')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)
    birthdate = models.DateField(blank=True, null=True)
    mobile_no = models.IntegerField(unique=True)
    user_type = models.CharField(choices=user_types,
                                 default='Customer',
                                 max_length=9)

    def is_user_authenticated(self, yes=True):
        self.is_authenticated = yes
