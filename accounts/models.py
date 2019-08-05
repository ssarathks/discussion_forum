from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Details(models.Model):
    user=models.OneToOneField(User,related_name='details')
    branch=models.CharField(max_length=264)
    semester=models.CharField(max_length=264)

    def __str__(self):
        return self.user.username


class Items(models.Model):
    user=models.ForeignKey(User,related_name='items')
    name=models.CharField(max_length=263)
    category=models.CharField(max_length=253)

    def __str__(self):
        return self.name
