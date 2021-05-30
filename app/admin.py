from django.contrib import admin
from .models import Entry, Store, Category, Item

# Register your models here.

admin.site.register(Entry)
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Item)