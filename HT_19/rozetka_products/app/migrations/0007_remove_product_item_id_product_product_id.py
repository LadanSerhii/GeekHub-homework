# Generated by Django 4.1.5 on 2023-01-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_inputfield_productlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='item_id',
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='No id', max_length=20),
        ),
    ]
