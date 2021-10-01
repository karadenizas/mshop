from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('mycartadd/<int:product_id>/', views.my_cart_add, name='my_cart_add'),
    path('mycart/', views.my_cart, name='my_cart'),
]
