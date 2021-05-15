from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(response):
	return render(response, "app/home.html")

def add_entry(response):
	if response.method=="POST":
		form = EntryForm(response.POST)
		if form.is_valid:
			model = form.save(commit=False)
			model.save()
	else:
		form = EntryForm()
	return render(response, "app/add_entry.html", {'form': form})