from django.urls import path
from .views import ProductList, ProductListCreateView

urlpatterns = [
    # path('products/', ProductList.as_view(), name='product-list'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
]