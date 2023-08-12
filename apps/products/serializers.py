from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'discount',
            'price_discount',
            'discount_percentage',
        ]

    def validate_discount(self, value):
        if value == 0:
            value = 1
            return value
        try:
            value = value / 100
            return value
        except:
            raise serializers.ValidationError('Invalid discount value')
