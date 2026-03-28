from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=120, unique=True)
	logo = models.ImageField(upload_to='categories/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=150)
	stock = models.PositiveIntegerField(default=0)
	image = models.ImageField(upload_to='products/')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

	def __str__(self):
		return self.name
