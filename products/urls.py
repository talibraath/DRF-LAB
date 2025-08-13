from django.urls import path
from .views import ProductList, ProductListCreateView,ProductDetailView, ProductViewSet,ProductModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')
router.register(r'products', ProductModelViewSet, basename='productmodel')

urlpatterns = [
    # path('products/', ProductList.as_view(), name='product-list'),
    # path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    # path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

] + router.urls