import pytest

from apps.product.models import Personal


# Import the factory here

@pytest.mark.django_db
def test_model2():
    personal = Personal.objects.create(first_name='John', last_name='Doe', age=20, tall=9.99)
    assert personal.first_name == 'John'
    assert personal.last_name == 'Doe'
    assert personal.age == 20
    assert personal.tall == 9.99


@pytest.mark.django_db
def test_category_model(category_factory):
    z = category_factory()
    assert z.__str__() == 'category'


@pytest.mark.django_db
def test_brand_model(brand_factory):
    x = brand_factory()
    assert x.__str__() == 'brand'


@pytest.mark.django_db
def test_product_model(product_factory):
    name = product_factory()
    assert name.__str__() == 'product'

#finishing the __str__ function test
