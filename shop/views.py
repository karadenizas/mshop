from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm


def index(request, category_slug=None):
    category = None
    products = None
    paginate_products = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        try:
            paginate_products = paginator.page(page)
        except PageNotAnInteger:
            paginate_products = paginator.page(1)
        except EmptyPage:
            paginate_products = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'products': products,
        'paginate_products': paginate_products,
    }

    return render(request, 'shop/index.html', context)

def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    context = {
        'categories': categories,
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/product_detail.html', context)


def test(request):
    return render(request, 'test.html')