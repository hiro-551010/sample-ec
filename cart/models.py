
from django.db import models


from accounts.models import User
from datetime import datetime
from front.models import Product


class Cart(models.Model):
    cart_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Cart')
    data_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['data_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True,)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'CartItem'


    def sub_total(self):
        return self.product.price * self.quantity
 
    def __str__(self):
        return self.product
