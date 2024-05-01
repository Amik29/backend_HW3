from django.db import models

# Create your models here.
class Profile(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=40)
    post_base = models.CharField(max_length=10000)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
