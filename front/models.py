from django.db import models
from django.db.models.fields import IntegerField
from config import settings
from accounts.models import Profile, User

class Product(models.Model):
    name = models.CharField("商品名", max_length=250)
    price = models.IntegerField("値段", default=0)
    detail = models.TextField("詳細", default="商品詳細")
    image = models.ImageField("写真", upload_to='image/')
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name



class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quantity = IntegerField(null=True)
    product = models.CharField(default='商品名', max_length=100)
    price = models.IntegerField(null=True)
    stripe_id = models.CharField(max_length=1000)
    order_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orderhistory'

"""
class Orders(models.Model):
    total_price = models.PositiveBigIntegerField()
    address = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'orders'

class OrderItems(models.Model):
    quantity = models.PositiveBigIntegerField()
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_items'
        unique_together = [['prodct', 'order']]
"""






