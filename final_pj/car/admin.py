from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_type', 'model', 'year', 'emission_standard']
    list_filter = ['car_type', 'model', 'year']
    ordering = ['-year']
    search_fields = ['car_type', 'model', 'year']


