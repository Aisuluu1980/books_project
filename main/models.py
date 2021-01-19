from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    price = models.CharField(max_length=8)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=150)
    year = models.CharField(max_length=4)
    date = models.DateTimeField(auto_now=True)
    is_favorite = models.BooleanField(default=False)
