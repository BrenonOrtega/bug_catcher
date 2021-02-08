from django.contrib import admin
from .models import Error

@admin.register(Error)
class ErrorModel(admin.ModelAdmin):
    list_filter = ('name', 'author', 'date')
    list_display = ('name', 'author', 'date')

    #date_hierarchy = ...
    #ordering = ...
