
import pytest
from infra.clients.api_client_flask_api import APIClientRestAPI

@pytest.fixture
def setup(context_api):
    api_client = APIClientRestAPI(context_api)
    yield api_client

class TestRestAPI:

    def test_get_restful(self, setup):
        api_client = setup
        found_person = api_client.restful_get_person_by_id(2)
        assert found_person['person']['name'] == 'chad'
        ''' test ready '''

    def test_add_new_person_restful(self, setup):
        api_client = setup
        name = 'gustavo'
        age = 35
        gender = 'male'
        api_client.restful_add_person(name, age, gender)
        person = api_client.restful_get_person_by_name(name)
        assert person['person']['name'] == name
        ''' test ready '''

    def test_edit_person_restful(self, setup):
        api_client = setup
        name = 'gustavo'
        new_name = 'gustava'
        new_age = 34
        new_gender = 'female'
        api_client.restful_edit_person(name, new_name, new_age, new_gender)
        person = api_client.restful_get_person_by_name(new_name)
        assert person['person']['gender'] == new_gender
        ''' test ready '''    

    def test_delete_person_restful(self, setup):
        api_client = setup
        name = 'gustava'
        api_client.restful_delete_person(name)
        response = api_client.restful_get_person_by_id(name)
        assert response['status'] == 404
        ''' test ready '''
    

        
