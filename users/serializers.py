from .models import User
from rest_framework import serializers


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):  #serializers.ModelSerializer

    class Meta:
        model = User
        fields = ['name','cc', 'email','telefono', 'direccion']


