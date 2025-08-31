from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']


# Register your models here.
admin.site.register(Item,ItemAdmin)
admin.site.register(User, UserAdmin)