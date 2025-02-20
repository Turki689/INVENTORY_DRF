from django.urls import path

from .views import ProductListCreateAPIView, ProductDetail, BrandDetailAPIView, BrandListAPIView, ProductFilterAPIView

urlpatterns = [
    path('products', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('brands/', BrandListAPIView.as_view(), name='brands'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name='brand-detail'),
    path('categories/<int:category_id>/products/', ProductFilterAPIView.as_view(), name='products-by-category'),
    # path('person/',PersonListCreateAPIView.as_view(),name='person')

]

app_name = 'product'
