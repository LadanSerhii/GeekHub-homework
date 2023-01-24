# Generated by Django 4.1.5 on 2023-01-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(default='No id', max_length=20)),
                ('title', models.CharField(default='No title', max_length=30)),
                ('old_price', models.FloatField(default=0)),
                ('current_price', models.FloatField(default=0)),
                ('href', models.CharField(default='No href', max_length=50)),
                ('brand', models.CharField(default='No Brand', max_length=30)),
                ('category', models.CharField(default='No category', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_list', models.TextField()),
            ],
        ),
    ]
