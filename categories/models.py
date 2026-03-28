from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=120, unique=True)
	logo = models.ImageField(upload_to='categories/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'products_category'

	def __str__(self):
		return self.name
