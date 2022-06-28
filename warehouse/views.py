from django.shortcuts import render
from importlib.abc import ResourceReader
import re
import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import product, cart, order
from .serializers import productSerializer, cartSerializer, orderSerializer
# from warehouse import serializers

# Create your views here.

class viewProduct(APIView):
    def post(self, request):
        try:
            productsAsItem = product.objects.get(productName=request.data["productName"])
            productsSerialized = productSerializer(productsAsItem, many=False)
            return Response({
                "status": 200,
                "data": productsSerialized.data
            })
        except Exception as e:
            return Response({
                "status": 400,
                "data": {},
                "error message": e.__str__()
            })

class products(APIView):
    def get(self, request):
        try:
            productsAsItem = product.objects.all()
            productsSerialized = productSerializer(productsAsItem, many=True)
            return Response({
                "status": 200,
                "data": productsSerialized.data
            })
        except Exception as e:
            return Response({
                "status": 400,
                "data": {},
                "error message": e.__str__()
            })

    def post(self, request):
        try:
            productSerializedData = productSerializer(data = request.data)

            if productSerializedData.is_valid():
                productSerializedData.save()
                return Response({
                    "status": status.HTTP_200_OK,
                    "data": productSerializedData.data,
                    "message": "Product added successfully"
                })
            else:
                print(dir(productSerializedData))
                return Response({
                    "status": 400,
                    "data": {},
                    "message": productSerializedData.errors
                })
        except Exception as e:
            return Response({
                "status": 500,
                "data": {},
                "error message": e
            })


class carts(APIView):
    def post(self, request):
        try:
            product_details = product.objects.get(productName=request.data["productName"])
            Cart = cart(productName = product_details, quantity = request.data['quantity'])
            # print(Cart)
            if True:
            # serializer = cartSerializer(data=request.data)
            # if serializer.is_valid():
                # Cart = cart(
                #     productName = product_details.productName,
                #     quantity = request.data['quantity']
                # )
                Cart.save()
                # serializer.save()
                return Response(
                    {
                        "status": "success",
                        "data": {},
                        # "serializer data": serializer.data
                        # "productDetails": product_details
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response({
                    "status": 500,
                    "data": {},
                    "message": serializer.errors
                })
        except Exception as e:
            return Response({
                "status": 400,
                "data": {},
                "message": e.__str__()
            })

    def delete(self, request):
        try:
            cart_instance = cart.objects.get(productName = request.data["productName"])
            print(cart_instance)
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "data": {},
                    "message": e.__str__()
                },
                status=status.HTTP_200_OK
            )
        cart_instance.delete()
        return Response(
            {
                "status": "success",
                "data": {},
                "message": "deleted"
            },
            status=status.HTTP_200_OK
        )


class placeOrder(APIView):
    def post(self, request):
        # cart_instance = cart.objects.get(productName=request.data["productName"])
        carts = cart.objects.all()
        items = []
        for cart_instance in carts:
            items.append(cart_instance.productName.productName)

            serializer = orderSerializer(data=cart_instance)

            Product_name = cart_instance.productName
            pin_code = request.data["pinCode"]
            delivery_time = request.data["deliveryTime"]
            Quantity = cart_instance.quantity
            
            cart_instance.delete()
            # cart_id.save()

            Order = order(
                productName = Product_name,
                pinCode = pin_code,
                quantity = Quantity,
                deliveryTime = delivery_time
            )

            Order.save()

            print(serializer.is_valid())
            print(Order)

        return Response(
            {
                "status": "success",
                "data": items
            },
            status=status.HTTP_200_OK
        )