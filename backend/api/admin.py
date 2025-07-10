from django.contrib import admin
from .models import Product, Location, Transaction

admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Transaction)

