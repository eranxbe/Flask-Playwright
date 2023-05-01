from infra.utils.config import FLASK_URL
from infra.utils.api_client import APIClient

class APIClientRestAPI(APIClient):
    def __init__(self, context_api):
        super().__init__(context_api)
        self.base_url = f'{FLASK_URL}/rest'

    def get_person_by_id(self, id):
        return self.get_request(f'person/{id}')
    
    def get_person_by_name(self, name):
        return self.get_request(f'person/{name}')
    
    def get_all_person(self):
        return self.get_request('get-all')

    def add_person(self, name, age, gender):
        data = {
            "name" : str(name),
            "age" : int(age),
            "gender" : str(gender)
        }
        return self.post_request('/add-person', data=data)
    

    # def change_person(self, id, name, age, gender):
    #     data = {
    #         "id": id,
    #         "name" : name,
    #         "age" : age,
    #         "gender" : gender
    #     }
    #     return self.put_request('/change-person', data=data)
    
    def delete_person(self, name):
        data = {
            "name" : name
        }
        return self.delete_request(f'/delete-person', data=data)
    

    
