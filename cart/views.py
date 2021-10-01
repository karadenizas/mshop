from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .models import Mycart
from django.http import HttpResponse
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@login_required
@require_POST
def my_cart_add(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    control_product = Mycart.objects.filter(user=user)
    if control_product.filter(product_id=product_id):
        messages.error(request, 'This product is available in your cart now. Please, update in your cart!')
        return redirect('cart:my_cart')
    elif form.is_valid():
        cd = form.cleaned_data
        m_cart = Mycart.objects.update_or_create(user=user, product=product, quantity=cd['quantity'], price=product.price)
    return redirect('cart:my_cart')



@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial=
                                       {'quantity': item['quantity'],
                                        'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})


@login_required
def my_cart(request):
    user = request.user
    product = Mycart.objects.filter(user=user)
    # for item in product:
    #     if item
    context = {
        'product': product,
    }
    return render(request, 'cart/my_cart.html', context)