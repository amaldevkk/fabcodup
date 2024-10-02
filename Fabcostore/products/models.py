from django.db import models
from django.utils import timezone
# Create your models here.
# models.py



class Product(models.Model):
    CATEGORY_CHOICES = [
        ('women', 'Women\'s Wear'),
        ('men', 'Men\'s Wear'),
        ('baby', 'Baby Wear'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField( default=timezone.now)
    def __str__(self):
        return self.name
    

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.product.name}'


