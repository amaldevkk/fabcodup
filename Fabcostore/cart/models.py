from django.db import models
from products .models import Product
from django.contrib.auth.models import User



# Create your models here.
class Cartitem(models.Model):
    SIZE_CHOICES = [
       
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} * {self.product.name} ({self.size})'

    