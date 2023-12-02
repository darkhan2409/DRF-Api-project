from rest_framework.serializers import ModelSerializer
from .models import *


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['title', 'username', 'password', 'email', 'director', 'bin', 'address', 'phone']

    def create(self, validated_data):
        supplier = Supplier.objects.create(**validated_data)
        supplier.set_password(validated_data['password'])
        supplier.save()
        return supplier


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['title', 'username', 'description', 'bin', 'director', 'address', 'email', 'phone']


class SupplierUpdateSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['description', 'email', 'director', 'address', 'phone']


