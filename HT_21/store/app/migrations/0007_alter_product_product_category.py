# Generated by Django 4.1.5 on 2023-02-01 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_product_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.productcategory'),
        ),
    ]
