from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ProductCrud(APIView):
    def get(self,request,id):
        # PDO = Product.objects.all()
        # SDO = ProductSerializer(PDO, many = True)
        PDO = Product.objects.get(id=id)
        SDO = ProductSerializer(PDO)

        return Response(SDO.data,status=status.HTTP_200_OK)

    def post(self,request,id):
        
        SDO = ProductSerializer(data = request.data)
        if SDO.is_valid():
            SDO.save()
            return Response({'POST':'data created successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'Error':'Data not in correct format'}, status=status.HTTP_404_NOT_FOUND)
        
        