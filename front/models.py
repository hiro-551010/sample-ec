from django.db import models



class Product(models.Model):
    product_name = models.CharField("商品名",max_length=250)
    price = models.IntegerField("値段",default=0)
    detail = models.TextField("詳細", default="商品詳細")
    image = models.ImageField("写真", upload_to='image/')

    def __str__(self):
        return self.product_name


