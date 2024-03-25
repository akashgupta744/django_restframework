from rest_framework import serializers
from app.models import *

class ProductModSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'