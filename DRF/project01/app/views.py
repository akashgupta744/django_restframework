from django.http import HttpResponse
from django.shortcuts import render
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Products_json_data(request):
    POD = Products.objects.all()
    JOD = ProductModelSerializers(POD, many = True)
    
    return Response(JOD.data)

def productfun(request):
    obj = Products(product_no = 10, product_name='pencil', product_price = 30, product_desc = 'snaxhzm ')
    print(obj)
    return HttpResponse(' hsbxz k')
    e