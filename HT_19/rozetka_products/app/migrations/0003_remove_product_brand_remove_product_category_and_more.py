# Generated by Django 4.1.5 on 2023-01-16 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='current_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='href',
        ),
        migrations.RemoveField(
            model_name='product',
            name='old_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
