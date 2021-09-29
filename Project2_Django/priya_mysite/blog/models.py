from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, verbose_name='Author of blog', on_delete=models.CASCADE)
    SELECT_GENDER = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=SELECT_GENDER, default='null')
    date_of_birth = models.DateField(help_text='Please use the following format:<em>dd/mm/yyyy</em>')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(UserInfo, verbose_name='related to blog Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=164)
    text = models.TextField()
    SELECT_DESIGNATION = [('VICE PRESIDENT', 'Vice President'),
                          ('MANAGER', 'Manager'),
                          ('TEAM LEAD', 'Team Lead'),
                          ('CHIEF INFORMATION OFFICER', 'Chief Information Officer'),

                          ]
    designation = models.CharField(max_length=30, choices=SELECT_DESIGNATION, default='VICE PRESIDENT')
    create_data = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_data = timezone.now()
        self.save()

    # Only approved comments will be visible with the posts
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # after creating a post, user navigates to 'post_detail' view
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    random_author = models.CharField(max_length=164)
    text = models.TextField()
    create_data = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    # after entering a comment, user navigates to the post_list view
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text



