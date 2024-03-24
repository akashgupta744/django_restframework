from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    Category_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length = 100)
    product_brand = models.CharField(max_length = 100)

