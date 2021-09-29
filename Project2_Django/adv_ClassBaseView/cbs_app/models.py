from django.db import models
from django.urls import reverse


# Create your models here.
class School(models.Model):

    name = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cbs_app:detail', kwargs={'pk': self.pk})
        #return reverse('cbs_app:list')


class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
