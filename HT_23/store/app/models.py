from django.db import models


class ProductList(models.Model):
    product_list = models.TextField()


class Product(models.Model):
    item_id = models.CharField(max_length=20, default='No id')
    title = models.CharField(max_length=200, default='No title')
    old_price = models.FloatField(default=0)
    current_price = models.FloatField(default=0)
    href = models.CharField(max_length=50, default='No href')
    brand = models.CharField(max_length=30, default='No Brand')
    category = models.CharField(max_length=30, default='No category')
    product_category = models.ForeignKey('ProductCategory', on_delete=models.DO_NOTHING, default=1, null=True)

    def get_absolute_url(self):
        return f'/products/{self.id}/'

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    category_id = models.CharField(max_length=30, default='No category id')
    category_name = models.CharField(max_length=30, default='No category')

    def __str__(self):
        return self.category_name


