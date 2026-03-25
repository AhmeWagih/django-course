from django.http import HttpResponse
from django.shortcuts import render

products = [
  {"id":1, "name":"Product one", "stock": 10, "price": 1000,"image":"images/1.jpg","description":"This is a description"},
  {"id":2, "name":"Product two", "stock": 20, "price": 2000,"image":"images/2.jpg","description":"This is a description"},
  {"id":3, "name":"Product three", "stock": 30, "price": 3000,"image":"images/3.jpg","description":"This is a description"},
  {"id":4, "name":"Product four", "stock": 40, "price": 4000,"image":"images/4.jpg","description":"This is a description"},
  {"id":5, "name":"Product five", "stock": 50, "price": 5000,"image":"images/5.jpg","description":"This is a description"},
  {"id":6, "name":"Product six", "stock": 60, "price": 6000,"image":"images/6.jpg","description":"This is a description"},
]

def home(request):
  return render(request, 'products/home.html')

def index(request):
  return render(request, 'products/index.html', {'products': products})

def detail(request, id):
  product_found = filter(lambda product: product['id'] == id, products)
  product_found = list(product_found)

  if len(product_found) == 0:
    return HttpResponse("<h1 style='color:red'> No product found</h1>")

  product = product_found[0]
  return render(request, 'products/detail.html', {'product': product})

