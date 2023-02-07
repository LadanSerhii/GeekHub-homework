from django import forms

from .models import ProductList, Product


class InputForm(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = ['product_list', ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item_id', 'title', 'old_price', 'current_price', 'href', 'brand', 'category', 'product_category']
