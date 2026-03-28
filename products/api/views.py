from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from categories.api.serializers import CategorySerializer
from categories.models import Category
from products.api.serializers import ProductSerializer
from products.models import Product


@api_view(["GET","POST"])
def product_list(request):
  if request.method == "POST":
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)

@api_view(["GET","PATCH","DELETE"])
def product_detail(request,product_id:int):
  product = get_object_or_404(Product, pk=product_id)
  if request.method == "GET":
    serializer = ProductSerializer(product)
    return Response(serializer.data)
  elif request.method == "PATCH":
    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(["GET","POST"])
def category_list(request):
  if request.method == "POST":
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  categories = Category.objects.all()
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)