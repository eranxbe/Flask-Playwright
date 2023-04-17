import pytest
from infra.clients.api_client_chuck_norris import APIClientChuckNorris


class TestChuckNorrisAPI:
    @pytest.mark.usefixtures("context_api")
    def test_get_random_joke(self, context_api):
        client = APIClientChuckNorris(context_api)
        joke = client.get_random_joke()
        assert joke['value'] is not None

    @pytest.mark.usefixtures("context_api")
    def test_get_categories(self, context_api):
        expected_count = 16
        client = APIClientChuckNorris(context_api)
        categories = client.get_list_of_categories()
        assert categories is not None
        assert len(categories) == expected_count