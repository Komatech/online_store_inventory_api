import django_filters
from inventory.models import Item, Supplier, Supply

class ItemFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    date_added = django_filters.DateFilter(field_name="date_added")

    class Meta:
        model = Item
        fields = ['name', 'min_price', 'max_price', 'date_added', 'suppliers']

class SupplierFilter(django_filters.FilterSet):
    class Meta:
        model = Supplier
        fields = ['name','country','city','state','items']

class SupplyFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date_supplied", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="date_supplied", lookup_expr='lte')

    class Meta:
        model = Supply
        fields = ['item', 'supplier', 'start_date', 'end_date']
