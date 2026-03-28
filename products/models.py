from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=100)
	stock = models.PositiveIntegerField()
	image = models.ImageField(upload_to='products/')
	price = models.IntegerField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='products')

	def __str__(self):
		return self.name
