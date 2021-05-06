from django.db import models
from config import settings


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
    email = models.CharField(default='購入者Eメール', blank=False, null=False, max_length=100)
    product = models.CharField(default='商品名', max_length=100)
    price = models.IntegerField(null=True)
    stripe_id = models.CharField(max_length=1000)
    order_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orderhistory'




