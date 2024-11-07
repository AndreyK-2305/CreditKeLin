# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ProductType, Product
from decimal import Decimal

class ProductTypeTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product_type1 = ProductType.objects.create(name='Test ProductType', status='active')
        cls.product_type2 = ProductType.objects.create(name='Another ProductType', status='inactive')

    @classmethod
    def tearDownClass(cls):
        Product.objects.all().delete()
        ProductType.objects.all().delete()
        super().tearDownClass()

    def test_get_product_type_list(self):
        url = reverse('producttype-list')
        response = self.client.get(url, format='json')
        print(response.data)
        self.assertEqual(len(response.data), 2)

    def test_get_product_type_detail(self):
        url = reverse('producttype-detail', kwargs={'pk': self.product_type1.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product_type1.name)

    def test_create_product_type(self):
        url = reverse('producttype-list')
        data = {
            'name': 'New ProductType',
            'status': 'inactive'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProductTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product_type = ProductType.objects.create(name='Test ProductType', status='active')
        cls.product = Product.objects.create(
            type_product=cls.product_type,
            price=Decimal('50.00'),
            product_name='Test Product',
            description='Test Description',
            available=10
        )

    @classmethod
    def tearDownClass(cls):
        Product.objects.all().delete()
        ProductType.objects.all().delete()
        super().tearDownClass()

    def test_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_product_detail(self):
        url = reverse('product-detail', kwargs={'pk': self.product.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_name'], self.product.product_name)

    def test_create_product(self):
        url = reverse('product-list')
        type_product_url = reverse('producttype-detail', kwargs={'pk': self.product_type.id})
        data = {
            'type_product': type_product_url,
            'price': Decimal('75.00'),
            'product_name': 'New Product',
            'description': 'New Description',
            'available': 5
        }
        response = self.client.post(url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
