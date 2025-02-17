from django.urls import path

from .views import ProductListCreateAPIView, ProductDetail, BrandDetailAPIView, BrandListAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('brands/', BrandListAPIView.as_view(), name='brands'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name='brand-detail')
    # path('person/',PersonListCreateAPIView.as_view(),name='person')

]
