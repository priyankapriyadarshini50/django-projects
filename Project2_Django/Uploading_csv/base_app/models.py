from django.db import models


# Create your models here.
class UserData(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=246)
    gender = models.CharField(max_length=150)
    ip_address = models.FloatField(unique=True)
    city = models.CharField(max_length=150)


