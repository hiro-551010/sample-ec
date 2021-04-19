from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
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
        (None,{
            'fields': (
                'user',
                'username',
                'zipcode',
                'city',
                'address',
            )
        })
    )
admin.site.register(User)

