from rest_framework import serializers
from inventory.models import Item, Supplier

class ItemLookupField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'name': value.name
        }

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise serializers.ValidationError("Expected a string representing a numeric ID.")
        try:
            item = Item.objects.get(id=int(data))
        except Item.DoesNotExist:
            raise serializers.ValidationError("Item with does not exist.")
        return item

class SupplierSerializer(serializers.ModelSerializer):
    items = ItemLookupField(many=True, queryset=Item.objects.all(), required=False)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'phone', 'country', 'city', 'state', 'zip', 'address', 'email', 'items']
