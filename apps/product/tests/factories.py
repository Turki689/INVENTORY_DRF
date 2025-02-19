import factory

from apps.product.models import Category, Product, Brand


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'category'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = 'brand'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = 'product'
    description = 'lorem ipsum'
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
