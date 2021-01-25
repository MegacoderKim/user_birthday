import pytest


@pytest.fixture
@pytest.mark.django_db
def get_api_key():
    from rest_framework_api_key.models import APIKey

    api_key, key = APIKey.objects.create_key(name="test-service")
    return key


@pytest.fixture
def api_client(get_api_key):
    from rest_framework.test import APIClient

    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION="Api-Key " + get_api_key)
    yield api_client
    api_client.credentials(HTTP_AUTHORIZATION=None)
