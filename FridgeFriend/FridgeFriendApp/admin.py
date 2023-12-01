from django.contrib import admin
from . import models

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'quantity', 'expiry_date', 'fridge']
    
