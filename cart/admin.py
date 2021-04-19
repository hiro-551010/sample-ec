from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    model = Cart

class CartItemAdmin(admin.ModelAdmin):
    model = CartItem