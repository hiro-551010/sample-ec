# Generated by Django 3.2.1 on 2021-05-06 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_orderhistory_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
