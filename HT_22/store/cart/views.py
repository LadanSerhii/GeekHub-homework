import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse

from app.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(product=product, quantity=form.cleaned_data['quantity'], update_quantity=form.cleaned_data['update'])
    context = {
        'cart': cart,
    }
    return redirect('cart_detail')
    # return render(request, 'cart.html', context)


@login_required
@require_GET
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


@require_GET
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    context = {
        'cart': cart,
    }
    return render(request, 'cart.html', context)


@login_required
# @require_GET
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')


class CartView(View):
    template_name = 'cart.html'

    def delete(self, request):
        cart = Cart(self.request)
        cart.clear()
        return JsonResponse({"success": True}, status=204)

    def patch(self, request):
        data = json.loads(request.body)
        cart = Cart(request)
        product_id = data['product_id']
        cart.remove_by_id(product_id)
        return JsonResponse({
            "success": True,
            "cart_total_price": str(cart.get_total_price()),
        }, status=200)

    def post(self, request):
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product, product_quantity, True)
        cart.save()
        return JsonResponse({
            "success": True,
            "product_quantity": product_quantity,
            "product_total_price": str(product.current_price * product_quantity),
            "cart_total_price": str(cart.get_total_price()),
        }, status=200)





