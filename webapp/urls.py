from django.urls import path
from webapp.views import products_view

urlpatterns = [
    path('', products_view, name='products'),
    path('products', products_view, name='products_list'),
]