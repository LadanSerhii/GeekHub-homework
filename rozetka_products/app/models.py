from django.db import models

class InputField(models.Model):
    product_list = models.TextField()

class Product(models.Model):
    item_id = models.CharField(max_length=20, default='No id')
    title = models.CharField(max_length=30, default='No title')
    old_price = models.FloatField(default=0)
    current_price = models.FloatField(default=0)
    href = models.CharField(max_length=50, default='No href')
    brand = models.CharField(max_length=30, default='No Barnd')
    category = models.CharField(max_length=30, default='No category')

    def get_absolute_url(self):
        return f'/products/{self.id}/'