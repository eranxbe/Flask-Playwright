
import pytest
from infra.clients.api_client_flask_api import APIClientRestAPI

class TestRestAPI:
    @pytest.mark.usefixtures("context_api")
    def test_get_person_by_id(self, context_api):
        client = APIClientRestAPI(context_api)
        person = client.get_person_by_id('2')
        assert person['name'] == 'Jane Doe'
        assert person['gender'] == 'female'

    @pytest.mark.usefixtures("context_api")
    def test_search_person(self, context_api):
        client = APIClientRestAPI(context_api)
        person = client.search_person(name='gustavo')
        assert person['name'] == 'gustavo'
        assert person['gender'] == 'Male'

    @pytest.mark.usefixtures("context_api")
    def test_add_person(self, context_api):
        p_name = "mike"
        p_age = "33"
        p_gender = "male"
        client = APIClientRestAPI(context_api)
        person = client.add_person(p_name, p_age, p_gender)
        assert person['name'] == p_name
        assert person['gender'] == p_gender

    @pytest.mark.usefixtures("context_api")
    def test_delete_person_by_id(self, context_api):
        client = APIClientRestAPI(context_api)
        last_person = client.search_person(name='mike', age=33)
        response = client.delete_person_by_id(last_person['id'])
        assert response.status == 204
    

        
