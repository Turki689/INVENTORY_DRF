from rest_framework.generics import ListAPIView

from apps.brand.serializers.brand_serializers import BrandSerializer
from .models import Brand


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# Create your views here.
