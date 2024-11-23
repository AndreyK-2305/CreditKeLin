# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(
            name='Test User',
            cc=123456789,
            email='test@example.com',
            telefono=1234567890,
            direccion='123 Test St'
        )

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        super().tearDownClass()

    def test_get_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_user_detail(self):
        url = reverse('user-detail', kwargs={'pk': self.user.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.user.name)

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'name': 'New User',
            'cc': 987654321,
            'email': 'newuser@example.com',
            'telefono': 9876543210,
            'direccion': '456 New St'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user(self):
        url = reverse('user-detail', kwargs={'pk': self.user.id})
        data = {
            'name': 'Updated User',
            'cc': 123456789,
            'email': 'updated@example.com',
            'telefono': 1234567890,
            'direccion': '123 Updated St'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])

    def test_partial_update_user(self):
        url = reverse('user-detail', kwargs={'pk': self.user.id})
        data = {
            'telefono': 9876543210
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['telefono'], data['telefono'])

    def test_delete_user(self):
        url = reverse('user-detail', kwargs={'pk': self.user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
