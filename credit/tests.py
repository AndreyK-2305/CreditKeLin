from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Credit, Payment, User
from products.models import Product, ProductType
from decimal import Decimal

class CreditAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(name='testuser', cc=123456789, email='test@example.com', telefono=1234567890, direccion='Test Address')
        self.product_type = ProductType.objects.create(name='Electronics', status='active')
        self.product = Product.objects.create(type_product=self.product_type, price=100.00, product_name='Test Product', description='A test product', available=10)
        self.client.force_authenticate(user=self.user)
        self.credit_url = reverse('credit-list')
        self.payment_url = lambda pk: reverse('credit-payments', kwargs={'pk': pk})
        self.data = {
            "client": self.user.id,
            "product": self.product.id,
            "status": "active",
            "total_payments": 12
        }

    def test_create_credit(self):
        data = {
            'client': self.user.id,
            'status': 'active',
            'product': self.product.id,
            'debt': '100.00',
            'total_payments': 2
        }
        response = self.client.post(self.credit_url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Credit.objects.count(), 1)
        self.assertEqual(Credit.objects.get().debt, Decimal('110.00'))
        self.assertEqual(Payment.objects.filter(credit=Credit.objects.get()).count(), 2)

    def test_get_payments_for_credit(self):
        credit = Credit.objects.create(client=self.user, status='active', product=self.product, debt='50.00')
        Payment.objects.create(credit=credit, value=25.00)
        Payment.objects.create(credit=credit, value=25.00)

        response = self.client.get(self.payment_url(credit.id), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['value'], '25.00')
        self.assertEqual(response.data[1]['value'], '25.00')

    def test_create_credit_with_payments(self):
        response = self.client.post(self.credit_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        credit = Credit.objects.get(client=self.user)
        payments = Payment.objects.filter(credit=credit)
        self.assertEqual(payments.count(), self.data["total_payments"])
        self.assertEqual(Product.objects.get(id=self.product.id).available, 9)

    def test_create_credit_no_stock(self):
        self.product.available = 0
        self.product.save()

        response = self.client.post(self.credit_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('No products in stock', str(response.data))
