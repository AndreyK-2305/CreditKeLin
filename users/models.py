from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    cc = models.IntegerField(null=False)
    email = models.CharField(max_length=30, null=False)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    @property
    def is_authenticated(self):
        return True
