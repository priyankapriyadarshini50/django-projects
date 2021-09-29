from django.db import models


# Create your models here.
class UsersInformation(models.Model):
    QUALIFICATION = [
        ('UG', 'Under Graduate'),
        ('G', 'Graduate'),
        ('PG', 'Post Graduate'),
        ('PhD', 'Doctor of Philosophy')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=128, unique=True)
    qualification = models.CharField(max_length=10, choices=QUALIFICATION)

    def __str__(self):
        return self.first_name
