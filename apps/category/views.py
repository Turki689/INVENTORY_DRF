from rest_framework.generics import ListCreateAPIView
from apps.category.models import Category
from apps.category.serializers.category_serializer import CategorySerializer


# class CategoryViewSet(viewsets.ViewSet):
#     queryset = Category.objects.all()
#
#     def list(self, request, *args, **kwargs):
#         serializer = CategorySerializer(self.queryset, many=True)
#         return Response(
#             serializer.data
#         )


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Create your views here.
