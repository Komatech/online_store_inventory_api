from rest_framework import viewsets, permissions
from inventory.models import Item
from inventory.serializers.item import ItemSerializer
from rest_framework.pagination import PageNumberPagination
from inventory.filters import ItemFilter
from django_filters.rest_framework import DjangoFilterBackend

class ItemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter
    pagination_class = ItemPagination
