from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.base, name='base'),
    path('<slug:category_slug>/', views.base, name='category_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]