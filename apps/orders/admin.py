from django.contrib import admin
from .models import Order, ProductOrder, Invoice

admin.site.register(Order)
admin.site.register(ProductOrder)
admin.site.register(Invoice)

