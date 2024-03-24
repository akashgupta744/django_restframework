from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_id','product_name','product_brand')


