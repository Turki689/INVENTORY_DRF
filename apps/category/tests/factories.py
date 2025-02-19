import factory
from factory.django import DjangoModelFactory

from apps.category.models import Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'Category_%d' % n)
