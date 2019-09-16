from django.db import models

# Create your models here.
class StockURL(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)