from django.db import models

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
    
#Credit
class Credit(models.Model):
    
    CREDITSTATUSES = {
        "started": "Started",
        "active": "Active",
        "completed": "Completed",
        "suspended": "Suspended"
    }
    Credit_id = models.IntegerField(null=False)
    #Client_id = models.ForeignKey('User', on_delete=models.SET_NULL)
    Status = models.CharField(choices=CREDITSTATUSES, max_length=10)
    Created_at = models.DateField(null=False)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    #Payment_id = models.ForeignKey('Payment', on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name
    #Payment
class Payment(models.Model):

    PAYMENTSTATUSES = {
        "pending": "Pending",
        "delayed": "Delayed",
        "completed": "Completed"
    }

    Payment_id = models.IntegerField(null=False)
    Payment_STATUS = models.CharField(max_length=10)
    Value = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    Delayed_Value = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name
