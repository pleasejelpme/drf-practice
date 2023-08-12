from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveAPIView, 
    ListCreateAPIView, 
    RetrieveUpdateAPIView, 
    RetrieveDestroyAPIView
    )
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
from django.http import Http404

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


# @api_view(['GET', 'POST'])
# def products(request, *args, **kwargs):
#     if request.method == 'GET':
#         instance = Product.objects.all()
#         data = ProductSerializer(instance, many=True).data
#         return Response(data)

#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             product = serializer.save()
#             print(product)
#             return Response(serializer.data)
#         return Response({'error':'Invalid data'}, status=400)


# LIST AND CREATE PRODUCTS
class ProductListCreateAPIVIEW(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# DETAIL PRODUCT
class ProductDetailAPIVIEW(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# UPDATE PRODUCT
class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     if not instance.description:
    #         instance.description = instance.name
    #     return super().perform_update(serializer)


# DELETE PRODUCT

class ProductDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer








# Renaming views for urls
create_list_product = ProductListCreateAPIVIEW.as_view()
detail_product = ProductDetailAPIVIEW.as_view()
update_product = ProductUpdateAPIView.as_view()
delete_product = ProductDestroyAPIView.as_view()
