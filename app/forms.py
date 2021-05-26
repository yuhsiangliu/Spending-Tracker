from django import forms
from django.forms import ModelForm
from .models import Category, Store, Entry, Item

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'color']
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'color': forms.Select(attrs={'class': 'form-control', }),
        }

class StoreForm(ModelForm):
	class Meta:
		model = Store
		fields = ['name', 'location']
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'location': forms.TextInput(attrs={'class': 'form-control', }),
        }


class EntryForm(ModelForm):
	class Meta:
		model = Entry
		fields = ['name', 'cost', 'date', 'category', 'store', 'note']
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'cost': forms.NumberInput(attrs={'class': 'form-control', }),
            'date': forms.DateInput(attrs={'class': 'form-control', }),
            'category': forms.Select(attrs={'class': 'form-control', }),
            'store': forms.Select(attrs={'class': 'form-control', }),
            'note': forms.TextInput(attrs={'class': 'form-control', }),
        }

class ItemForm(ModelForm): 
	class Meta:
		model = Item
		fields = ['name', 'amount', 'price', 'entry']
