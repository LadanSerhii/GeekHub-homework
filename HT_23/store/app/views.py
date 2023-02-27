# import subprocess

# 25165361,138685031,59013970,59036506,138684310,55599132,55598190

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets

from .models import Product, ProductCategory, ProductList
from .forms import InputForm, ProductForm
from cart.forms import CartAddProductForm
from .serializers import ProductCategorySerializer, ProductSerializer, ProductListSerializer

from .tasks import scrape_products


def add_products(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():
                form.save()
                form = InputForm()
                scrape_products.delay()
        else:
            form = InputForm()
        context = {
            'form': form,
        }
        return render(request, 'input.html', context)
    else:
        return render(request, 'main.html', {})


def products(request):
    all_products = Product.objects.all()
    all_categories = ProductCategory.objects.all()
    product_context = {
        'all_products': all_products,
        'all_categories': all_categories,
    }
    return render(request, 'products.html', product_context)


def category_view(request, category_id):
    current_category = get_object_or_404(ProductCategory.objects.filter(id=category_id))
    all_categories = ProductCategory.objects.all()
    all_products = Product.objects.filter(product_category=current_category)
    context = {
        'all_products': all_products,
        'current_category': current_category,
        'all_categories': all_categories,
    }
    return render(request, 'products.html', context)


def single_product_view(request, product_id):
    product = get_object_or_404(Product.objects.filter(id=product_id))
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'detail.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {})
        login(request, user)
        return redirect('/')
    return render(request, 'login.html', {})


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('products')
    return render(request, 'logout.html', {})


def delete_view(request, product_id):
    if request.user.is_superuser:
        context = {}
        current_product = get_object_or_404(Product, id=product_id)
        if request.method == "POST":
            current_product.delete()
            return redirect('products')
        return render(request, "products.html", context)
    else:
        messages.info(request, 'You have not permissions!')
        return redirect('products')


def create_view(request):
    if request.user.is_superuser:
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('detail.html')
        context = {
            'product_form': product_form,
        }
        return render(request, "create_view.html", context)
    else:
        messages.info(request, 'You have not permissions!')
        return redirect('products')


def update_view(request, product_id):
    if request.user.is_superuser:
        product = Product.objects.get(id=product_id)
        if request.method == 'POST':
            product_form = ProductForm(request.POST, instance=product)
            if product_form.is_valid():
                product_form.save()
                return redirect('products')
        else:
            product_form = ProductForm(instance=product)
        context = {
            'product_form': product_form,
        }
        return render(request, 'update_detail.html', context)
    else:
        messages.info(request, 'You have not permissions!')
        return redirect('products')


class ProductCategoryView(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductListView(viewsets.ModelViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
