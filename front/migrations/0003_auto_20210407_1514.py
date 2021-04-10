# Generated by Django 3.1.7 on 2021-04-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20210406_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(default='商品詳細', verbose_name='詳細'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='商品詳細', upload_to='images', verbose_name='写真'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='値段'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=250, verbose_name='商品名'),
        ),
    ]