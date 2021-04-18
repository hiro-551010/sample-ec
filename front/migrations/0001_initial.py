# Generated by Django 3.1.7 on 2021-04-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250, verbose_name='商品名')),
                ('price', models.IntegerField(default=0, verbose_name='値段')),
                ('detail', models.TextField(default='商品詳細', verbose_name='詳細')),
                ('image', models.ImageField(upload_to='image/', verbose_name='写真')),
            ],
        ),
    ]
