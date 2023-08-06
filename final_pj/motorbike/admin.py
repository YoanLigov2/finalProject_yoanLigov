from django.contrib import admin
from .models import Motorbike


@admin.register(Motorbike)
class MotorbikeAdmin(admin.ModelAdmin):
    list_display = ['bike_type', 'model', 'year', 'engine_size']
    list_filter = ['bike_type', 'model', 'year']
    ordering = ['-year']
    search_fields = ['bike_type', 'model', 'year']
