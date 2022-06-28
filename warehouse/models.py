from django.db import models
import json

# Create your models here.
class product(models.Model):
    productName = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=50)
    MRP = models.DecimalField(max_digits=8, decimal_places=4)
    SP = models.DecimalField(max_digits=8, decimal_places=4)
    category = models.CharField(max_length=20)

    def __str__(self):
        # JsonResponse = {"productName": self.productName, "description":self.description, "MRP": str(self.MRP), "SP": str(self.SP), "category": self.category}
        return str(self.productName)
        # return json.dumps(JsonResponse)

class cart(models.Model):
    productName = models.ForeignKey(product, on_delete=models.CASCADE, primary_key=True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.productName)

class order(models.Model):
    productName = models.ForeignKey(product, on_delete=models.CASCADE, primary_key=True)
    quantity = models.IntegerField()
    pinCode = models.IntegerField()
    deliveryTime = models.DateTimeField()

    def __str__(self):
        return str(self.productName)