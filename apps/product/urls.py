from django.urls import path

from .views import ProductListCreateAPIView, ProductDetail, BrandDetailAPIView, BrandListAPIView, ProductFilterAPIView, \
    ProductlinesFromProduct

urlpatterns = [
    path('products', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('brands/', BrandListAPIView.as_view(), name='brands'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name='brand-detail'),
    path('categories/<int:category_id>/products/', ProductFilterAPIView.as_view(), name='products-by-category'),
    path('products/<slug:slug>/productlines/', ProductlinesFromProduct.as_view(), name='list'),

    # path('person/',PersonListCreateAPIView.as_view(),name='person')

]

app_name = 'product'
