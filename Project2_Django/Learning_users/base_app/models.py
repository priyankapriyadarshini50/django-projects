from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Create some additional fields to UserProfileInfo Table
    portfolio_link = models.URLField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username
