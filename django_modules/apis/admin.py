from django.contrib import admin
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Products, ProductsAdmin)
