from django.utils import timezone

from django.db import models


# Create your models here.

class User(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="Your Name", null=False)
    age = models.IntegerField(default=18, null=True)
    gender = models.CharField(default='M', max_length=7, null=False)
    timestamp = models.DateTimeField(default=timezone.now)
    uname = models.CharField(unique=True, max_length=255, default="Username", null=False)
    country = models.CharField(max_length=255, default="Country", null=False)
    password = models.CharField(max_length=1024, default="Password", null=False)
    high_score = models.IntegerField(default=0, null=True)


class Question(models.Model):
    _id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255, null=False, default="Default Question Is It ?")
    optionA = models.CharField(max_length=250, default='A', null=False)
    optionB = models.CharField(max_length=250, default='B', null=False)
    optionC = models.CharField(max_length=250, default='C', null=False)
    optionD = models.CharField(max_length=250, default='D', null=False)
    ans = models.CharField(max_length=3, default='A', null=False)
