from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):  #serializers.ModelSerializer

    class Meta:
        model = User
        fields = ['id','name','cc', 'email','telefono', 'direccion']


