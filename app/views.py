from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
import csv

def home(request):
	return render(request, "app/home.html")

def add_entry(request):
	if request.method=="POST":
		form = EntryForm(request.POST)
		if form.is_valid:
			model = form.save(commit=False)
			model.save()
	else:
		form = EntryForm()
	return render(request, "app/add_entry.html", {'form': form})

def entry_list(request):
	all_entries = Entry.objects.all().order_by('-date')
	params = {
		"entries": all_entries
	}
	if request.method=="POST":
		if "download-data" in request.POST:
			response = HttpResponse('text/csv')
			response['Content-Disposition'] = 'attachment; filename=all_expenses.csv'
			writer = csv.writer(response)
			writer.writerow(['Date', 'Category', 'Store', 'Amount'])
			for entry in all_entries:
				writer.writerow([str(entry.date), entry.category, entry.store, entry.cost])
			return response
		elif "add-entry" in request.POST:	
			form = EntryForm(request.POST)
			if form.is_valid:
				model = form.save(commit=False)
				model.save()
		elif "add-category" in request.POST:
			form_c = CategoryForm(request.POST)
			if form_c.is_valid:
				model = form_c.save(commit=False)
				model.save()
		elif "add-store" in request.POST:
			form_s = StoreForm(request.POST)
			if form_s.is_valid:
				model = form_s.save(commit=False)
				model.save()
	params["form"] = EntryForm()
	params["form_c"] = CategoryForm()
	params["form_s"] = StoreForm()
	return render(request, "app/entry_list.html", params)