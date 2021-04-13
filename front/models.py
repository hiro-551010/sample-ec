from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    product_name = models.CharField("商品名",max_length=250)
    price = models.IntegerField("値段",default=0)
    detail = models.TextField("詳細", default="商品詳細")
    image = models.ImageField("写真", upload_to='image/')

    def __str__(self):
        return self.product_name

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), unique=True, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(default="匿名ユーザー",max_length=30)
    zipcode = models.CharField(default="", max_length=8)
    prefecture = models.CharField(default="", max_length=6)
    city = models.CharField(default="", max_length=100)
    address = models.CharField(default="", max_length=200)
