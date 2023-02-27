from rest_framework import serializers

from .models import Product, ProductCategory, ProductList


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['url', 'category_id', 'category_name']


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductList
        fields = ['product_list']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['item_id', 'title', 'old_price', 'current_price', 'href', 'brand', 'category', 'product_category']

