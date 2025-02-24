from rest_framework import serializers

from apps.product_line.models import ProductLine


# class ProductLineSerializer(serializers.ModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())  # Ensure product is required
#
#     class Meta:
#         model = ProductLine
#         fields = ['id', 'name', 'price', 'stock_quantity', 'is_active', 'product']
#         read_only_fields = ['id']
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['category'] = instance.product.category.name
#         data['brand'] = instance.product.brand.name
#         data['product'] = instance.product.name
#         return data


class ProductLineSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True, allow_null=True)

    # category_name = serializers.CharField(source='product.category.name', read_only=True)
    # brand_name = serializers.CharField(source='product.brand.name', read_only=True)

    class Meta:
        model = ProductLine
        fields = ['id', 'name', 'price', 'stock_quantity', 'is_active', 'product_name']
        read_only_fileds = ['id']
