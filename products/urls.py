from django.urls import path
from .views import ProductList, ProductListCreateView,ProductDetailView

urlpatterns = [
    # path('products/', ProductList.as_view(), name='product-list'),
    # path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

]