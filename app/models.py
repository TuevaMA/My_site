from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True) #ключевое
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    foto = models.CharField(max_length=50)
