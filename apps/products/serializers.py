from rest_framework import serializers

from .validators import validate_name, validate_discount, validate_stock
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    update_url = serializers.HyperlinkedIdentityField(view_name='product-update', lookup_field='pk')
    delete_url = serializers.HyperlinkedIdentityField(view_name='product-delete', lookup_field='pk')
    name = serializers.CharField(validators=[validate_name])
    stock = serializers.IntegerField(validators=[validate_stock])
    discount = serializers.IntegerField(validators=[validate_discount])

    class Meta:
        model = Product
        fields = [
            'id',
            'detail_url',
            'update_url',
            'delete_url',
            'name',
            'description',
            'price',
            'stock',
            'discount',
            'price_discount',
            'discount_percentage',
        ]

