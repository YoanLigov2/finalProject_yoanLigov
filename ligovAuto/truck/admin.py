from django.contrib import admin
from .models import Truck


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ['model', 'year', 'truck_mass', 'truck_height']
    list_filter = ['model', 'year']
    ordering = ['-year']
    search_fields = ['model', 'year']
