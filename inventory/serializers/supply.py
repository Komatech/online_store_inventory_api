from rest_framework import serializers
from inventory.models import Item, Supplier, Supply
from inventory.serializers.item import SupplierLookupField
from inventory.serializers.supplier import ItemLookupField

class SupplySerializer(serializers.ModelSerializer):
    supplier = SupplierLookupField(many=False, queryset=Supplier.objects.all(), required=False)
    item = ItemLookupField(many=False, queryset=Item.objects.all(), required=False)
    class Meta:
        model = Supply
        fields = ['id', 'item', 'supplier', 'quantity', 'date_supplied']
