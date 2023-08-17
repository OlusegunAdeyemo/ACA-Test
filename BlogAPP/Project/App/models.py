from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, null=True)
    firstname = models.CharField(max_length=25, null=True)
    lastname = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True)
    password = models.CharField(max_length=50, null=False)


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=250, null=False)
    creation_date = models.CharField(max_length=250, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
