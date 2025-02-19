from pytest_factoryboy import register

from .factories import CategoryFactory, ProductFactory, BrandFactory

register(CategoryFactory)
register(ProductFactory)
register(BrandFactory)
