# Generated by Django 3.2.1 on 2021-05-07 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('username', models.CharField(default='匿名ユーザー', max_length=30)),
                ('zipcode', models.CharField(default='', max_length=8)),
                ('prefecture', models.CharField(default='', max_length=5)),
                ('city', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
