from django.db import models
import django.urls
import django.utils.timezone
# Create your models here.

#ProductTypeModel
class ProductType(models.Model):
    STATUSES = {
        "active": "Active",
        "inactive": "Inactive"
    }
    name = models.CharField(max_length=511, null=False)
    status = models.CharField(max_length=55, choices=STATUSES)

    def __str__(self) -> str:
        return self.name
    
#Product
class Product(models.Model):
    Product_id = models.IntegerField(null=False)
    Type_Product_Id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    Price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    Product_Name = models.CharField(null=False, max_length=30)
    Description = models.CharField(max_length=100)
    Available = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.name
    
#User
class User(models.Model):
    Client_id = models.IntegerField(null=False)
    name = models.CharField(max_length=20, null=False)
    cc = models.IntegerField()
    username = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=15)

#Payment
class Payment(models.Model):

    PAYMENTSTATUSES = {
        "pending": "Pending",
        "delayed": "Delayed",
        "completed": "Completed"
    }
    Payment_id = models.IntegerField(null=False)
    Payment_STATUS = models.CharField(max_length=10)
    Value = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)
    Delayed_Value = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.name

#Credit
class Credit(models.Model):
    CREDITSTATUSES = {
        "started": "Started",
        "active": "Active",
        "completed": "Completed",
        "suspended": "Suspended"
    }
    Credit_id = models.IntegerField(null=False)
    Client_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    Status = models.CharField(choices=CREDITSTATUSES, max_length=10)
    Created_at = models.DateField(null=False, default= django.utils.timezone.now)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
