
class APIClient:
    def __init__(self, context_api):
        self.context_api = context_api

    def get_request(self, path: str, data = None):
        url = f'{self.base_url}/{path}'
        response = self.context_api.get(url, params=data)
        return response.json()

    def post_request(self, path: str, data = None):
        url = f'{self.base_url}/{path}'
        response = self.context_api.post(url, params=data)
        return response.json()
    
    def put_request(self, path: str, data = None):
        url = f'{self.base_url}/{path}'
        response = self.context_api.put(url, params=data)
        return response.json()
    
    def delete_request(self, path: str, data = None):
        url = f'{self.base_url}/{path}'
        response = self.context_api.delete(url, params=data)
        return response