from django.db import models

# Create your models here.
#User
class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    cc = models.IntegerField()
    username = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.name


