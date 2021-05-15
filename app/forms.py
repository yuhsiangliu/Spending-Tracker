from django.forms import ModelForm
from .models import Category, Store, Entry, Item

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'color']

class StoreForm(ModelForm):
	class Meta:
		model = Store
		fields = ['name', 'location']


class EntryForm(ModelForm):
	class Meta:
		model = Entry
		fields = ['name', 'cost', 'date', 'category', 'store', 'note']


class ItemForm(ModelForm): 
	class Meta:
		model = Item
		fields = ['name', 'amount', 'price', 'entry']
