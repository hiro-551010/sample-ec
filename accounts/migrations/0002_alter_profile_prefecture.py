# Generated by Django 3.2 on 2021-05-05 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefecture',
            field=models.CharField(default='', max_length=5),
        ),
    ]
