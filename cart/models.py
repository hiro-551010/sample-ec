
from django.db import models


from accounts.models import User
from datetime import datetime
from front.models import Product
from accounts.models import Profile


class Cart(models.Model):
    cart = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, primary_key=True, )

    class Meta:
        db_table = 'Cart'

    def __int__(self):
        return self.cart


class CartItemManager(models.Manager):
    def save_item(self, product_id, quantity, cart):
        c = self.model(quantity=quantity, product_id=product_id, cart=cart)
        c.save()


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)    
    quantity = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    objects = CartItemManager()
    #price = models.OneToOneField(Product.pk.price, on_delete=models.CASCADE)
    #price_ht = models.FloatField(blank=True)

    class Meta:
        db_table = 'CartItem'
        unique_together = [['product', 'cart']]
    """
    def sub_total(self):
        tax_amount = 1.1
        return tax_amount * self.product.price_ht * self.quantity
    """
    def __str__(self):
        return self.product

