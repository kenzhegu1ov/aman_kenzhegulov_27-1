from django.db import models
from django.db import models


# Create your models here.


class Products(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.FloatField()
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)




