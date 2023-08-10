from django.contrib import admin
from .models import Yacht


@admin.register(Yacht)
class YachtAdmin(admin.ModelAdmin):
    list_display = ['style', 'classification', 'engines', 'yacht_length']
    list_filter = ['style', 'classification', 'engines']
    ordering = ['-yacht_length']
    search_fields = ['style', 'classification', 'engines']
