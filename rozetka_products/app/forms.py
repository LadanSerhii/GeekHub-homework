from django import forms


from .models import Product, InputField

class InputForm(forms.ModelForm):
    class Meta:
        model = InputField
        fields = ['product_list',]
