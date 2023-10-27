from rest_framework import serializers
from .models import Item, ItemStatus

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "item_name", "quantity", "expiry_date", "fridge", "category"]
        
