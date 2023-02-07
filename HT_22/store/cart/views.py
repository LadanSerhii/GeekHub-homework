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
    return redirect('cart_detail')


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
@require_GET
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')


class CartClearView(View):
    template_name = 'cart.html'

    def get(self, *args, **kwargs):
        text = 'It is text for testing!'
        if self.request.is_ajax():
            return JsonResponse({'text': text}, status=200)
        return redirect('cart_detail')

    def post(self, request):
        if self.request.method == "POST" and self.request.is_ajax():
            cart = Cart(self.request)
            cart.clear()
            form = self.form_class(self.request.POST)
            form.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=400)


