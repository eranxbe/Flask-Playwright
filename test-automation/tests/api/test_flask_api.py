
import pytest
from infra.clients.api_client_flask_api import APIClientRestAPI

@pytest.fixture(scope="module")
def api_client(context_api):
    return APIClientRestAPI(context_api)

class TestRestAPI:


    def test_get_user_by_name(self, api_client):
        expected_name = 'mike'
        actual_person = api_client.get_person_by_name(expected_name)
        assert actual_person['name'] == expected_name
    ''' test ready '''

    def test_get_all(self, api_client):
        person_list = api_client.get_all_person()
        print(person_list)
        assert person_list[0]['gender'] == 'male'
    ''' test ready ''' 

    def test_add_person(self, api_client):
        p_name = "lukas"
        p_age = 42
        p_gender = "male"
        api_client.add_person(name=p_name, age=p_age, gender=p_gender)
        expected_person = api_client.get_person_by_name(p_name)
        assert expected_person['name'] == p_name
    ''' test ready '''    

    def test_delete_person(self, api_client):
        person_name = "lukas"
        api_client.delete_person(person_name)
        response = api_client.get_person_by_name(person_name)
        assert response['status'] == 404
    ''' test ready '''

    ## create edit person test
    

        
