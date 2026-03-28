from django.urls import path

from categories import views


urlpatterns = [
    path('categories/<int:id>/', views.detail, name='category_detail'),
]
