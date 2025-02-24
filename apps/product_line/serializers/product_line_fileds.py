from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.product.models import Product
from apps.product_line.models import ProductLine


class ProductLineFiledsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = ['name', 'price', 'is_active', 'stock_quantity']

    def create(self, validated_data):
        # Retrieve the product using the slug from the view kwargs
        product_slug = self.context['view'].kwargs['slug']
        product = get_object_or_404(Product, slug=product_slug)

        # Add product to the validated_data
        validated_data['product'] = product

        # Create and return the ProductLine instance
        return ProductLine.objects.create(**validated_data)
