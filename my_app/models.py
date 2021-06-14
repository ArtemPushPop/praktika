from django.db import models
from random import choice


# Create your models here.

class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures')


class Post(models.Model):
    def __str__(self):
        return self.post

    user = models.CharField(max_length=40)
    post = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
