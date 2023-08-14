from rest_framework import serializers
from .models import Product

def validate_name(value):
    product_name = Product.objects.filter(name__iexact=value)
    if product_name.exists():
        raise serializers.ValidationError(f'product {value} already exist')
    return value

def validate_stock(value):
    if value < 0:
        raise serializers.ValidationError('Stock cannot be a negative number')
    return value

def validate_discount(value):
    if value >= 100 or value < 0:
        raise serializers.ValidationError('Discount has to be between 0 and 100')
    if value == 0 or value == None:
        value = 1
        return value
        
    value = value / 100
    return value
