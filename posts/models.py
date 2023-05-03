from django.db import models
from django.db import models


# Create your models here.


class Products(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.FloatField(default=5)
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=256)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)


    def __str__(self):
        return self.text

