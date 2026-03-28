from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'category', 'stock', 'price', 'created_at', 'updated_at')
	list_filter = ('category',)
	search_fields = ('name', 'description')
