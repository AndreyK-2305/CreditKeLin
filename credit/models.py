# models.py
from django.db import models
from products.models import Product
from users.models import User
from datetime import datetime

class Credit(models.Model):
    CREDITSTATUSES = [
        ("started", "Started"),
        ("active", "Active"),
        ("completed", "Completed"),
        ("suspended", "Suspended"),
    ]
    client = models.ForeignKey(User, on_delete=models.RESTRICT)
    status = models.CharField(choices=CREDITSTATUSES, max_length=10)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_payments = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.client} - {self.status}"

class Payment(models.Model):
    PAYMENTSTATUSES = [
        ("pending", "Pending"),
        ("delayed", "Delayed"),
        ("completed", "Completed"),
    ]
    payment_STATUS = models.CharField(max_length=10, choices=PAYMENTSTATUSES)
    value = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)
    delayed_value = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)
    credit = models.ForeignKey(Credit, related_name='payments', on_delete=models.RESTRICT)
    due_to = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.payment_STATUS
