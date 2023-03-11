from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=2550)
    image_url = models.CharField(max_length=2083)


class Offers (models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


