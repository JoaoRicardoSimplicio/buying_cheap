from django.urls import path

from main.views.main_views import Home
from main.views import product_views

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('product/create/', product_views.ProductCreate.as_view(), name='product_create'),
    path('product/list/', product_views.ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', product_views.ProductDetail.as_view(), name='product_detail')
]
