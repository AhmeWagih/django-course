from django.urls import path

from products.api.views import category_list, product_detail, product_list

urlpatterns = [
	path('products/', product_list, name='products_api_list'),
	path('products/<int:product_id>/', product_detail, name='products_api_detail'),
	path('categories/', category_list, name='categories_api_list'),
  path('categories/<int:category_id>/', category_list, name='categories_api_detail'),
]
