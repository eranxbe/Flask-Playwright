from infra.utils.config import FLASK_URL
from infra.utils.api_client import APIClient

class APIClientRestAPI(APIClient):
    def __init__(self, context_api):
        super().__init__(context_api)
        self.base_url = FLASK_URL

    def get_person_by_id(self, id):
        return self.get_request(f'person/{id}')
    
    def search_person(self, name: str = None, age: int = None):
        data = {
            "name" : name,
            "age" : age
        }
        response = self.get_request('/search', data=data)
        return response[0] if response else None

    def add_person(self, name, age, gender):
        data = {
            "name" : name,
            "age" : age,
            "gender" : gender
        }
        return self.post_request('/add-person', data=data)
    

    def change_person(self, id, name, age, gender):
        data = {
            "id": id,
            "name" : name,
            "age" : age,
            "gender" : gender
        }
        return self.put_request('/change-person', data=data)
    
    def delete_person_by_id(self, id):
        return self.delete_request(f'/delete-person/{id}')
    

    
