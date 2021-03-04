from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_slug>/', views.index, name='category_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]