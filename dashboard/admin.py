from django.contrib import admin

# Register your models here.
from .models import Product, Category ,Order


# Register your models here.
admin.site.register(Category )
admin.site.register(Product)
admin.site.register(Order)