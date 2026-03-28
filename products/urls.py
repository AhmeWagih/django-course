from django.urls import path

from products import views


urlpatterns = [
  path('', views.home, name='home'),
  path('products/', views.index, name='products_index'),
  path('products/create/', views.create_product, name='product_create'),
  path('products/<int:id>/', views.detail, name='product_detail'),
  path('products/<int:id>/edit/', views.update_product, name='product_update'),
  path('products/<int:id>/delete/', views.delete_product, name='product_delete'),
]
