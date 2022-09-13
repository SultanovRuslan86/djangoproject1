from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name = 'category', unique=True)

class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name='product', unique=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)