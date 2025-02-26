from django.shortcuts import get_object_or_404
from rest_framework import serializers


class BrandFiledSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        if isinstance(data, int):
            return get_object_or_404(self.queryset, pk=data)
        return self.queryset.objects.get_or_create(name=data)[0]
