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

def entry_list(response):
	all_entries = Entry.objects.all().order_by('-date')
	params = {
		"entries": all_entries
	}
	if response.method=="POST":
		if "add-entry" in response.POST:	
			form = EntryForm(response.POST)
			if form.is_valid:
				model = form.save(commit=False)
				model.save()
		elif "add-category" in response.POST:
			form_c = CategoryForm(response.POST)
			if form_c.is_valid:
				model = form_c.save(commit=False)
				model.save()
		elif "add-store" in response.POST:
			form_s = StoreForm(response.POST)
			if form_s.is_valid:
				model = form_s.save(commit=False)
				model.save()
	params["form"] = EntryForm()
	params["form_c"] = CategoryForm()
	params["form_s"] = StoreForm()
	return render(response, "app/entry_list.html", params)