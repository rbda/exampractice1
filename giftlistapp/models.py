from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=250)


class Clothes(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.CharField(max_length=30)
    name = models.CharField(max_length=250)
    # price
    # url
    # image


