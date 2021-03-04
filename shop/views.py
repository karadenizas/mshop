from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def base_navbar(request):
    categories = Category.objects.all()
    return render(request, 'base.html', {'categories': categories})

def base(request, category_slug=None):
    product = None
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'product': product,
    }
    return render(request, 'base.html', context)

def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'categories': categories,
        'product': product,
    }
    return render(request, 'shop/detail.html', context)