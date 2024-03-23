from django.db import models

# Create your models here.

class Products(models.Model):
    product_no = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length = 100)
    product_price = models.DecimalField(max_digits = 5, decimal_places = 2)
    product_desc = models.TextField()



