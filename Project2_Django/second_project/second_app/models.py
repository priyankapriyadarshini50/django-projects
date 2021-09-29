from django.db import models


# Create your models here.
class UserInfo(models.Model):
    QUALIFICATION = (
        ('UG', 'UnderGraduate'),
        ('G', 'Graduate'),
        ('PG', 'PostGraduate'),
        ('PhD', 'Doctor of Philosophy'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=128)
    qualification = models.CharField(max_length=10, choices=QUALIFICATION)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
