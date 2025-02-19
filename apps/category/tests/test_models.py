import pytest

category_test_name = "Category"


@pytest.mark.django_db
def test_str(category_factory):
    category = category_factory()
    assert category.__str__().startswith(category_test_name)


@pytest.mark.django_db
def test_creat(category_factory):
    category = category_factory()
    assert category.name.startswith(category_test_name)