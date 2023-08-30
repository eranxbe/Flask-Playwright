from infra.utils.config import FLASK_URL
from infra.utils.api_client import APIClient

class APIClientRestAPI(APIClient):
    def __init__(self, context_api):
        super().__init__(context_api)
        self.base_url = f'{FLASK_URL}/rest'
    
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
        return self.post_request('add-person', data=data)
    

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
        return self.delete_request(f'delete-person', data=data)
    

    def restful_get_person_by_id(self, id):
        return self.get_request(f'restful_person/{id}')
    
    def restful_get_person_by_name(self, name):
        return self.get_request(f'restful_person/{name}')

    def restful_add_person(self, name, age, gender):
        data = {
            "name" : str(name),
            "age" : int(age),
            "gender" : str(gender)
        }
        return self.post_request('restful_new_person', data=data)
    
    def restful_edit_person(self, id_or_name, new_name=None, new_age=None, new_gender=None):
        data = {
            "name": str(new_name),
            "age": int(new_age),
            "gender": str(new_gender)
        }
        return self.put_request(f'restful_person/{id_or_name}', data=data)

    def restful_delete_person(self, id_or_name):
        return self.delete_request(f'restful_person/{id_or_name}')
