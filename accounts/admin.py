from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin
from cart.models import Cart, CartItem
from front.models import OrderHistory

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CartInline(admin.StackedInline):
    model = Cart
    can_delete = False

"""
class OrderHistoryInline(admin.StackedInline):
    model = OrderHistory
    can_delete = False
"""

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline, CartInline)
    fieldsets = (
        (None,{
            'fields': (
                'email',
                'password',
            )
        }),
        (None,{
            'fields': (
                'is_active',
                'is_admin',
            )
        }),
    )

admin.site.register(User, CustomUserAdmin)

