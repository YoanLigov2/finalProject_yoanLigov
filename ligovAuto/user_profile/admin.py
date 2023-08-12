from django.contrib import admin
from .models import CollectionUser


@admin.register(CollectionUser)
class CollectionUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'gender']
    list_filter = ['username', 'first_name', 'last_name']
    ordering = ['-username']
    search_fields = ['username', 'first_name', 'last_name']
    
