from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.products.models import Product


@api_view(['GET'])
def home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}

    if model_data:
        data = model_to_dict(model_data)

    return Response(data)

