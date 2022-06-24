from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import FavoriteCity

User = get_user_model()

class FavoriteCityInline(admin.StackedInline):
    model = FavoriteCity
    extra = 1

class CustomUserAdmin(UserAdmin):
    # everything else
    fieldsets = UserAdmin.fieldsets
    inlines = UserAdmin.inlines + [FavoriteCityInline]

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)