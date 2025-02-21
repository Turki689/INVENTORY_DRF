from django.urls import path

from apps.product_line.views import ProductLineListView, ProductlineProductListView

urlpatterns = [
    path('', ProductLineListView.as_view(), name='product_line_list'),
    path('<str:product_name>/productlines/', ProductlineProductListView.as_view(), name='list')
]
