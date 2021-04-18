from django.contrib import admin
from .models import Product

class ProductsAdmin(admin.ModelAdmin):
    
    fields = [
        'product',
        'price',
        'detail',
        'image',
        ]
        
admin.site.register(Product, ProductsAdmin)