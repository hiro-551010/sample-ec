from django.contrib import admin
from .models import OrderHistory, Product

class ProductsAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'price',
        'detail',
        'image',
        ]
        
admin.site.register(Product, ProductsAdmin)
