# Generated by Django 4.1.5 on 2023-01-20 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_product_item_id_product_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='item_id',
        ),
    ]
