from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120, unique=True)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=1)

    
    def price_discount(self):
        if self.discount == 1.00:
            return f'{self.price}'
        
        price = float(self.price)
        discount = 1 - float(self.discount)
        return '%.2f' %(price * discount)
    
    def discount_percentage(self):
        if self.discount == 1.00:
            return f'no discount'
        return '-' + '%.0f' %(self.discount * 100) + '%' 
    
    def is_available(self):
        return self.stock > 0

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'