# Generated by Django 3.0.7 on 2021-02-13 08:16

import GROCERY.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Cart2',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'cart2',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150)),
                ('product_description', models.CharField(max_length=500)),
                ('category_id', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('product_ImgUrl', models.ImageField(blank=True, null=True, upload_to=GROCERY.models.upload_path)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_role', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
                ('user_phoneNo', models.IntegerField()),
                ('user_address', models.TextField(max_length=250)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]