from infra.utils.config import CHUCK_NORRIS_API_URL
from infra.utils.api_client import APIClient


class APIClientChuckNorris(APIClient):
    def __init__(self, context_api):        
        super().__init__(context_api)
        self.base_url = CHUCK_NORRIS_API_URL

    def get_random_joke(self):
        return self.get_request('/random')
    
    def get_random_joke_from_category(self, category):
        return self.get_request(f'/random?category={category}')
    
    def get_list_of_categories(self):
        return self.get_request('/categories')
    
    def get_joke_by_free_text(self, text):
        return self.get_request(f'/search?query={text}')

    

    