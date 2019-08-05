from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Thread(models.Model):
    name=models.CharField(max_length=264)
    description=models.TextField()
    user=models.ForeignKey(User,related_name='threads')
    created_time=models.DateTimeField(default=timezone.now())
    approved_time=models.DateTimeField(blank=True,null=True)
    approved_thread=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def approve_thread(self):
        self.approved_time=timezone.now()
        self.approve_thread=True
        self.save()

class Comments(models.Model):
    thread=models.ForeignKey(Thread,related_name='comments')
    comment=models.TextField()
    created_time=models.DateTimeField(default=timezone.now())
    approved_time=models.DateTimeField(blank=True,null=True)
    approved_comment=models.BooleanField(default=False)

    def __str__(self):
        return self.comment

    def approve_comment(self):
        self.approved_time=timezone.now()
        self.approved_comment=True
