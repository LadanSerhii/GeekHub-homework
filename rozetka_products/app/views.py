from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
import subprocess


from .forms import InputForm

def add_products(request):
    output = "Welcome on board! Let's make Rozetka products page!"
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    process = subprocess.run(["python", "scrape/task_1.py"], stdout=subprocess.PIPE)
    return render(request, 'input.html', context)

def products(request):
    queryset = Product.objects.all()
    product_context = {
        'object_list': queryset,
    }
    return render(request, 'products.html', product_context)

def single_product_view(request, product_id):
    obj = Product.objects.get(id=product_id)
    product_data = {
        'object': obj
    }
    return render(request, 'detail.html', product_data)
