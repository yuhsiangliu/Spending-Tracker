from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Store(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Entry(models.Model):
	name = models.CharField(max_length=200)
	cost = models.IntegerField()
	date = models.DateField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	store = models.ForeignKey(Store, on_delete=models.RESTRICT, null=True)

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=100)
	amount = models.IntegerField()
	price = models.IntegerField()
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
