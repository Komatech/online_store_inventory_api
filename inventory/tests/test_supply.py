from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from inventory.models import Item, Supplier, Supply

class SupplyTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_supply(self):
        supplier = Supplier.objects.create(name='Supplier A', phone='+2349067542234', country='Nigeria', city='Lekki', state='Lagos', zip='11099', address='123 Test road', email='test@example.com')
        item = Item.objects.create(name='Item A', description='Description of Item A', price='10.00', quantity=0)
        item.suppliers.add(supplier)
        url = reverse('supply-list')
        data = {'item': str(item.id), 'supplier': str(supplier.id), 'quantity': 50}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supply.objects.count(), 1)
        self.assertEqual(Item.objects.get().quantity, 50)

    def test_list_supply(self):
        url = reverse('supply-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)