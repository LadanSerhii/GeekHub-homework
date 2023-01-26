import subprocess

from django.shortcuts import render, get_object_or_404

from .models import Product
from .forms import InputForm
from cart.forms import CartAddProductForm


def add_products(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            form = InputForm()
            subprocess.run(["python", 'scraper.py'], stdout=subprocess.PIPE)
    else:
        form = InputForm()
    context = {
        'form': form,
    }
    return render(request, 'input.html', context)


def products(request):
    all_products = Product.objects.all()
    product_context = {
        'all_products': all_products,
    }
    return render(request, 'products.html', product_context)


def single_product_view(request, product_id):
    product = get_object_or_404(Product.objects.filter(id=product_id))
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'detail.html', context)

