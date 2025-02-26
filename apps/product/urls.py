from django.urls import path

from .views import ProductListCreateAPIView, ProductDetail, ProductFromCategory, ProductlinesFromProduct, \
    ProductFromBrand

urlpatterns = [
    path('products', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('categories/<int:category_id>/products', ProductFromCategory.as_view(), name='products-by-category'),
    path('products/<slug:slug>/productlines', ProductlinesFromProduct.as_view(), name='list'),
    path('brands/<slug:brand_slug>/products', ProductFromBrand.as_view(), name='brand')

    # path('person/',PersonListCreateAPIView.as_view(),name='person')

]

app_name = 'product'
