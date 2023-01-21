# Generated by Django 4.1.5 on 2023-01-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_product_brand_remove_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='No Barnd', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='No category', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='current_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='href',
            field=models.CharField(default='No href', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='No title', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_id',
            field=models.CharField(default='No id', max_length=20),
        ),
    ]
