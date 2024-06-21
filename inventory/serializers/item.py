from rest_framework import serializers
from inventory.models import Item, Supplier

class SupplierLookupField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'name': value.name
        }

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise serializers.ValidationError("Expected a string representing a numeric ID.")
        try:
            supplier = Supplier.objects.get(id=int(data))
        except Supplier.DoesNotExist:
            raise serializers.ValidationError("Supplier with does not exist.")
        return supplier

class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierLookupField(many=True, queryset=Supplier.objects.all(), required=False)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_added', 'quantity', 'suppliers']