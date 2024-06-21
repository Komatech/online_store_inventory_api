from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from inventory.models import Item, Supplier

class ItemTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.supplier = Supplier.objects.create(name='Supplier A', phone='+2349067542234', country='Nigeria', city='Lekki', state='Lagos', zip='11099', address='123 Test road', email='test@example.com')
        self.item = Item.objects.create(name='Item A', description='Description of Item A', price='10.00', quantity=0)
        self.item.suppliers.add(self.supplier)

    def test_create_item(self):
        url = reverse('item-list')
        data = {'name': 'Item B', 'description': 'Description of Item A', 'price': '10.00', 'quantity': 10, 'suppliers': [str(self.supplier.id)]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(Item.objects.get(id=response.json()['id']).name, 'Item B')

    def test_list_item(self):
        url = reverse('item-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.json()['count'],1)
        self.assertEqual(response.json()['results'][0]['name'],'Item A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_item(self):
        url = reverse('item-detail', args=[self.item.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.json()['name'],'Item A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        url = reverse('item-detail', args=[self.item.id])
        data = {
            'name': 'Updated Item A',
            'description': 'Updated Description of Item A',
            'price': '15.00',
            'quantity': 5,
            'suppliers': [str(self.supplier.id)]
        }
        response = self.client.put(url, data, format='json')
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item A')
        self.assertEqual(self.item.description, 'Updated Description of Item A')
        self.assertEqual(self.item.price, 15.00)
        self.assertEqual(self.item.quantity, 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        url = reverse('item-detail', args=[self.item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Item.objects.filter(id=self.item.id).exists())