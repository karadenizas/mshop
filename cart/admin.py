from django.contrib import admin
from .models import Mycart


@admin.register(Mycart)
class MycartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity']