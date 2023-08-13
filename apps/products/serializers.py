from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'stock',
            'discount',
            'price_discount',
            'discount_percentage',
        ]

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('Stock cannot be a negative number')
        return value

    def validate_discount(self, value):
        if value >= 100 or value < 0:
            raise serializers.ValidationError('Discount has to be between 0 and 100')
        
        if value == 0:
            value = 1
            return value
        
        value = value / 100
        return value

