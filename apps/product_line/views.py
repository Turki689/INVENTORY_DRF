from rest_framework.generics import ListCreateAPIView, ListAPIView

from apps.product_line.models import ProductLine
from apps.product_line.serializers.product_line_serializer import ProductLineSerializer


class ProductLineListView(ListCreateAPIView):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer


# Create your views here.
class ProductlineProductListView(ListAPIView):
    serializer_class = ProductLineSerializer

    def get_queryset(self):
        product = self.kwargs['product_name']
        queryset = ProductLine.objects.filter(product__name=product)
        return queryset
