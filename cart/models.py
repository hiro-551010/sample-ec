
from django.db import models


from accounts.models import User
from datetime import datetime
from front.models import Product
from accounts.models import Profile


class Cart(models.Model):
    cart = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, primary_key=True, related_name='Cart')
    #data_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        #ordering = ['data_added']

    def __int__(self):
        return self.cart

class CartItem(models.Model):
    product = models.ManyToManyField(Product, blank=True,)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)    
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)
    #price = models.OneToOneField(Product.pk.price, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        tax_amount = 1.1
        return tax_amount * self.product.price_ht * self.quantity
 
    def __str__(self):
        return self.product
