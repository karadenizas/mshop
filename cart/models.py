from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from shop.models import Product
from django.urls import reverse


class Mycart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=1)
    image = models.URLField(null=True)
    
    def __str__(self):
        return f'{self.product} , id={self.id}'

    def get_total_price(self):
        return self.price * self.quantity