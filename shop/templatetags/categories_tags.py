from django import template
from ..models import Category, Product

register = template.Library()


@register.inclusion_tag('shop/categories.html')
def categories_tags():
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return context