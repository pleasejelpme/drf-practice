from django.db import models
from django.contrib.auth.models import User

from apps.products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=50, null=True)

class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)




