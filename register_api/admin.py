from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugModel(admin.ModelAdmin):
    list_filter = ['date', 'last_update']
