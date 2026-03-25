from django.urls import path

from products import views


urlpatterns = [
  path('', views.home, name='home'),
  path('products/', views.index, name='products_index'),
  path('products/<int:id>/', views.detail, name='product_detail'),
]
