import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from apps.category.tests.factories import CategoryFactory

register(CategoryFactory)


@pytest.fixture
def api_client():
    return APIClient
