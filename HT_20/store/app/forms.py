from django import forms
from .models import ProductList


class InputForm(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = ['product_list',]
