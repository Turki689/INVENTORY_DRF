from rest_framework import serializers


class BrandFiledSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        if isinstance(data, int):
            return self.queryset.objects.get_object_404(pk=data)
        return self.queryset.objects.get_or_create(name=data)[0]
