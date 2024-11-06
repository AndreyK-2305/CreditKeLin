from itertools import product
from django.db import models

from products.models import Product 
from users.models import User

# Create your models here.
#Payment
class Payment(models.Model):

    PAYMENTSTATUSES = {
        "pending": "Pending",
        "delayed": "Delayed",
        "completed": "Completed"
    }
    payment_STATUS = models.CharField(max_length=10, choices=PAYMENTSTATUSES)
    value = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)
    delayed_value = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.payment_STATUS

#Credit
class Credit(models.Model):
    CREDITSTATUSES = {
        "started": "Started",
        "active": "Active",
        "completed": "Completed",
        "suspended": "Suspended"
    }
    client = models.ForeignKey(User, on_delete=models.RESTRICT, default=0)
    status = models.CharField(choices=CREDITSTATUSES, max_length=10)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    payment = models.ForeignKey('Payment', on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.status
    

