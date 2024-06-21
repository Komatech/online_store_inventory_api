from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from inventory.models import Supplier

class SupplierTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.supplier = Supplier.objects.create(name='Supplier A', phone='+2349067542234', country='Nigeria', city='Lekki', state='Lagos', zip='11099', address='123 Test road', email='test@example.com')

    def test_create_supplier(self):
        url = reverse('supplier-list')
        data = {'name': 'Supplier B', 'phone': '+2349067542234', 'country': 'Nigeria', 'city': 'Lekki','state': 'Lagos', 'zip':'11099','address': '123 Test road', 'email': 'test2@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 2)
        self.assertEqual(Supplier.objects.get(id=response.json()['id']).name, 'Supplier B')

    def test_list_supplier(self):
        url = reverse('supplier-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.json()['count'],1)
        self.assertEqual(response.json()['results'][0]['name'],'Supplier A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_supplier(self):
        url = reverse('supplier-detail', args=[self.supplier.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.json()['name'],'Supplier A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_supplier(self):
        url = reverse('supplier-detail', args=[self.supplier.id])
        data = {
            'name': 'Updated Supplier A', 'phone': '+2349067542254', 'country': 'Nigeria', 'city': 'Lekki','state': 'Lagos', 'zip':'11089','address': '125 Test road', 'email': 'test24@example.com'
        }
        response = self.client.put(url, data, format='json')
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'Updated Supplier A')
        self.assertEqual(self.supplier.phone, '+2349067542254')
        self.assertEqual(self.supplier.zip, '11089')
        self.assertEqual(self.supplier.email, 'test24@example.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_supplier(self):
        url = reverse('supplier-detail', args=[self.supplier.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Supplier.objects.filter(id=self.supplier.id).exists())
