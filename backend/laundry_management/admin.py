from django.contrib import admin
from .models import LaundryEvent, LaundryCloth


@admin.register(LaundryEvent)
class LaundryEventAdmin(admin.ModelAdmin):
    list_display = ("created_on", "id")


@admin.register(LaundryCloth)
class LaundryClothAdmin(admin.ModelAdmin):
    list_display = ("created_on", "id", "name", "laundry")

