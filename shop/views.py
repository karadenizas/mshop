from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request, category_slug=None):
    category = None
    products = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'shop/index.html', context)

def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'categories': categories,
        'product': product,
    }
    return render(request, 'shop/detail.html', context)