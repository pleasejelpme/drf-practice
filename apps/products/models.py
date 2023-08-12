from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
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
     

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'