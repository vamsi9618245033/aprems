from django.contrib import admin

# Register your models here.
from .models import User,Product
# admin.py in your app
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Avoid redundant registration
if not admin.site.is_registered(User):
    admin.site.register(User, UserAdmin)

admin.site.register(Product)

