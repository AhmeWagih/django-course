from django.shortcuts import get_object_or_404, redirect, render
from categories.models import Category
from .models import Product


def home(request):
  categories = Category.objects.all()[:3]
  return render(request, 'products/home.html', {'categories': categories})


def index(request):
  products = Product.objects.all()
  return render(request, 'products/index.html', {'products': products})


def detail(request, id):
  product = get_object_or_404(Product, pk=id)
  return render(request, 'products/detail.html', {'product': product})


def create_product(request):
  categories = Category.objects.all()
  
  if request.method == 'POST':
    category_id = request.POST.get('category')
    name = request.POST.get('name')
    stock = request.POST.get('stock')
    price = request.POST.get('price')
    description = request.POST.get('description')
    image = request.FILES.get('image')
    
    category = Category.objects.filter(pk=category_id).first()
    if not category:
      return redirect('products_index')

    Product.objects.create(
      category=category,
      name=name,
      stock=stock,
      price=price,
      description=description,
      image=image
    )
    return redirect('products_index')
  
  return render(request, 'products/form.html', {
    'categories': categories,
  })


def update_product(request, id):
  product = get_object_or_404(Product, pk=id)
  categories = Category.objects.all()
  
  if request.method == 'POST':
    category_id = request.POST.get('category')
    category = Category.objects.filter(pk=category_id).first()
    if category:
      product.category = category

    product.name = request.POST.get('name')
    product.stock = request.POST.get('stock')
    product.price = request.POST.get('price')
    product.description = request.POST.get('description')
    if request.FILES.get('image'):
      product.image = request.FILES.get('image')
    product.save()
    return redirect('product_detail', id=product.id)
  
  return render(request, 'products/form.html', {
    'product': product,
    'categories': categories,
  })


def delete_product(request, id):
  product = get_object_or_404(Product, pk=id)
  product.delete()
  return redirect('products_index')

