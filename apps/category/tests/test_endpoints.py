import json

import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = "/api/categories/"

    def test_list_categories(self, category_factory, api_client):
        category_factory.create_batch(10)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 10


    def test_create_category(self, api_client):
        payload = {
            "name": "New Category",  # Adjust fields based on your model
        }
        response = api_client().post(self.endpoint, data=payload, format="json")
        assert response.status_code == 201  # Ensure it returns a successful creation status
        assert response.data["name"] == "New Category"
