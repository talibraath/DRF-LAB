from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductModelSerializer, ProductCustomSerializer
from rest_framework import mixins, generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.
class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductCustomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductModelSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer