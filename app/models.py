from django.db import models

# Create your models here.

COLORS = [
	('blue', 'Blue'),
	('red', 'Red'),
	('yellow', 'Yellow'),
	('green', 'Green'),
	('white', 'White'),
	('black', 'Black')
]

class Category(models.Model):
	name = models.CharField(max_length=30)
	color = models.CharField(max_length=10, choices=COLORS)

	def __str__(self):
		return self.name

class Store(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=500)

	def __str__(self):
		return f"{self.name} ({self.location})"

class Entry(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	cost = models.FloatField()
	date = models.DateField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	store = models.ForeignKey(Store, on_delete=models.RESTRICT)
	note = models.CharField(max_length=500, null=True, blank=True)

	def __str__(self):
		return f"{self.store.name} - ${self.cost}"

class Item(models.Model):
	name = models.CharField(max_length=100)
	amount = models.IntegerField()
	price = models.FloatField()
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
