from django.db import models


# Create your models here.
class SchoolInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    languages = models.CharField(max_length=60, blank=True, null=True)
    contact_number = models.CharField(max_length=20)
    city = models.CharField(max_length=60, blank=True, null=True)
    zip = models.PositiveIntegerField()

    def __str__(self):
        return self.name


