from rest_framework import serializers

from apps.brand.models import Brand
from .brand_fields import BrandFiledSerializer


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'description', 'brand']
