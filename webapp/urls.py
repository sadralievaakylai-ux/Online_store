from django.urls import path
from webapp.views import (products_view,
                          product_view,
                          category_add_view,
                          product_add_view,
                          categories_view,
                          category_edit_view,
                          category_delete_view,
                          product_edit_view
                          )


urlpatterns = [
    path('', products_view, name='products'),
    path('products', products_view, name='products_list'),
    path('products/<int:pk>/', product_view, name='product'),
    path('categories/add', category_add_view, name='category_add'),
    path('products/add', product_add_view, name='product_add'),
    path('categories', categories_view, name='categories'),
    path('categories/<int:pk>/edit', category_edit_view, name='category_edit'),
    path('categories/<int:pk>/delete', category_delete_view, name='category_delete'),
    path('products/<int:pk>/edit', product_edit_view, name='product_edit'),
]