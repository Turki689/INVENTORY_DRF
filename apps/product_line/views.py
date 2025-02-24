from rest_framework.generics import CreateAPIView

from apps.product_line.models import ProductLine
from apps.product_line.serializers.product_line_serializer import ProductLineSerializer


class ProductLineListView(CreateAPIView):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer

# Create your views here.
