from dataclasses import field
from math import prod
from unittest.util import _MAX_LENGTH
from importlib_metadata import requires
from rest_framework import serializers
from .models import order, product, cart

class productNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ["productName"]

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model =  product
        # fields = ["productName", "description", "MRP", "SP", "category"]
        fields = ("__all__")

class cartSerializer(serializers.ModelSerializer):
    productName = serializers.CharField(required=True)
    class Meta:
        model = cart
        fields = ["productName", "quantity"]
        # fields = ("__all__")

    def get_productName(self, obj):
        print("OBJ: ", obj.data)
        return productNameSerializer(obj.productName).data

class orderSerializer(serializers.ModelSerializer):
    productName = serializers.CharField(required=True)

    class Meta:
        model = order
        fields = ["productName", "quantity", "pinCode", "deliveryTime"]
        # fields = ("__all__")

    def get_productName(self, obj):
        print("OBJ: ", obj.data)
        return productNameSerializer(obj.productName).data
