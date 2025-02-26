from django.urls import path

from .views import CategoryListCreateAPIView, CategoryDetailAPIView

urlpatterns = [
    path('', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('<slug:slug>/', CategoryDetailAPIView.as_view(), name='category-detail')
]
