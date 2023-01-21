import os
import subprocess

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductList
from .forms import InputForm


def add_products(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            form = InputForm()
            process =  subprocess.run(["python", 'scraper.py'], stdout=subprocess.PIPE)
    else:
        form = InputForm()
    context = {
        'form': form,
    }
    return render(request, 'input.html', context)


def products(request):
    queryset = Product.objects.all()
    product_context = {
        'object_list': queryset,
    }
    return render(request, 'products.html', product_context)

def single_product_view(request, product_id):
    obj = Product.objects.get_object_or_404(id=product_id)
    product_data = {
        'object': obj
    }
    return render(request, 'detail.html', product_data)
