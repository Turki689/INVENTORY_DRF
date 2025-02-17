import pytest

from apps.product.models import Personal


# Import the factory here
def test_model():
    assert 1 == 1


@pytest.mark.django_db
def test_model2():
    personal = Personal.objects.create(first_name='John', last_name='Doe', age=20, tall=9.99)
    assert personal.first_name == 'John'
    assert personal.last_name == 'Doe'
    assert personal.age == 20
    assert personal.tall == 9.99


@pytest.mark.django_db
def test_category_model(category_factory):
    x = category_factory()  # Force the name
    assert x.__str__() == 'hello'
