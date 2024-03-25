from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.serializers import *
# Create your views here.


class ProductCrud(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer