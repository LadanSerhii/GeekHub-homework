from django.contrib import admin

from .models import (
    Product, ProductCategory
)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'title', 'old_price', 'current_price', 'href', 'brand', 'category', 'product_category']


@admin.register(ProductCategory)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']
