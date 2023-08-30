import pytest
from infra.clients.api_client_chuck_norris import APIClientChuckNorris

@pytest.fixture
def setup(context_api):
    client = APIClientChuckNorris(context_api)
    yield client

class TestChuckNorrisAPI:

    def test_get_random_joke(self, setup):
        client = setup
        joke = client.get_random_joke()
        assert joke['value'] is not None

    def test_get_categories(self, setup):
        expected_count = 16
        client = setup
        categories = client.get_list_of_categories()
        assert categories is not None
        assert len(categories) == expected_count