from django.db import transaction
from rest_framework import serializers

from apps.category.models import Category
from apps.category.serializers.fields import CategoryField
from apps.product.models import Brand, Product
from .fields import BrandCateforyField


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'id']


# class ProductSerializers(serializers.ModelSerializer):
#     brand = serializers.CharField()
#     category = serializers.CharField()
#
#     class Meta:
#         model = Product
#         fields = ["id", "name", "brand", "category"]
#
#     def to_representation(self, instance):
#         """Convert ForeignKey fields to names when listing."""
#         data = super().to_representation(instance)
#         data["brand"] = instance.brand.name
#         data["category"] = instance.category.name
#         return data
#
#     def to_internal_value(self, data):
#
#         validated_data = super().to_internal_value(data)
#
#         brand_input = data.get("brand")
#         if isinstance(brand_input, int):
#             validated_data["brand"] = Brand.objects.get(id=brand_input)
#         else:
#             validated_data["brand"], _ = Brand.objects.get_or_create(name=brand_input)
#
#         category_input = data.get("category")
#         if isinstance(category_input, int):
#             validated_data["category"] = Category.objects.get(id=category_input)
#         else:
#             validated_data["category"], _ = Category.objects.get_or_create(name=category_input)
#
#         return validated_data


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandCateforyField(queryset=Brand.objects.all())
    category = CategoryField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ["id", "name", "brand", "category"]

    @transaction.atomic
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.brand = validated_data.get("brand", instance.brand)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance
