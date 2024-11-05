from itertools import product
from django.db import models

from CreditKeLin.products.models import User, Product

# Create your models here.
#Payment
class Payment(models.Model):

    PAYMENTSTATUSES = {
        "pending": "Pending",
        "delayed": "Delayed",
        "completed": "Completed"
    }
    Payment_STATUS = models.CharField(max_length=10, choices=PAYMENTSTATUSES)
    Value = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)
    Delayed_Value = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.Payment_STATUS

#Credit
class Credit(models.Model):
    CREDITSTATUSES = {
        "started": "Started",
        "active": "Active",
        "completed": "Completed",
        "suspended": "Suspended"
    }
    Client = models.ForeignKey(User, on_delete=models.RESTRICT, default=0)
    Status = models.CharField(choices=CREDITSTATUSES, max_length=10)
    #Created_at = models.DateField(null=False, default= django.utils.timezone.now)
    Product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    Payment = models.ForeignKey('Payment', on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.Status
    

