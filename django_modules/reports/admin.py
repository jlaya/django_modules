from django.contrib import admin
from django_modules.home.models import Products


class ProductsAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Products, ProductsAdmin)
