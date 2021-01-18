from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    price = models.IntegerField(max_length=6)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=150)
    year = models.CharField(max_length=4)
    date = models.DateField(auto_now=True)
