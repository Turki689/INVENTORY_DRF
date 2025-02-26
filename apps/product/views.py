# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from apps.product.serializers.serializers import *
from apps.product_line.models import ProductLine


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['name', 'category', 'brand', 'is_digital']

    # 🔥 Fix: Use double underscore to filter by related model's field
    search_fields = ['name', 'category__name', 'brand__name']

    ordering_fields = ['name']
    queryset = Product.objects.all()


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class ProductFromCategory(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category_id']
        queryset = Product.objects.filter(category=category)
        return queryset


class ProductlinesFromProduct(ListCreateAPIView):
    serializer_class = ProductLineFiledsSerializer

    def get_queryset(self):
        product_slug = self.kwargs['slug']
        queryset = ProductLine.objects.select_related("product").filter(product__slug=product_slug)
        return queryset


# filter the products from the brand
class ProductFromBrand(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        brand_slug = self.kwargs['brand_slug']
        queryset = Product.objects.select_related("brand").filter(brand__slug=brand_slug)
        return queryset
