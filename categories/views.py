from django.shortcuts import get_object_or_404, render

from .models import Category


def detail(request, id):
	category = get_object_or_404(Category, pk=id)
	products = category.products.all()
	return render(request, 'categories/detail.html', {
		'category': category,
		'products': products,
	})
