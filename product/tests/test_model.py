import pytest

from product.models import Personal


@pytest.mark.django_db
def test_model():
    personal = Personal.objects.create(first_name='John', last_name='Doe', age=20, tall=9.99)
    assert personal.first_name == 'John'
    assert personal.last_name == 'Doe'
    assert personal.age == 20
    assert personal.tall == 9.99

@pytest.mark.django_db
def test_model2():
    personal = Personal.objects.create(first_name='John', last_name='Doe', age=20, tall=9.99)
    assert personal.first_name == 'John'
    assert personal.last_name == 'Doe'
    assert personal.age == 20
    assert personal.tall == 9.99
