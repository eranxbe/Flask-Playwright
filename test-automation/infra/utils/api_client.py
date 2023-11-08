
import pytest

@pytest.mark.usefixtures("context_api")
class APIClient:
    def __init__(self, context_api, base_url):
        self.context_api = context_api
        self.base_url = base_url

    def _request(self, method, path: str, data=None):
        url = f'{self.base_url}/{path}'
        response = None

        if method == 'GET':
            response = self.context_api.get(url, data=data)
        elif method == 'POST':
            response = self.context_api.post(url, data=data)
        elif method == 'PUT':
            response = self.context_api.put(url, data=data)
        elif method == 'DELETE':
            response = self.context_api.delete(url, data=data)

        if response:
            return response.json()
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

    def get_request(self, path: str, data=None):
        return self._request('GET', path, data)

    def post_request(self, path: str, data=None):
        return self._request('POST', path, data)

    def put_request(self, path: str, data=None):
        return self._request('PUT', path, data)

    def delete_request(self, path: str, data=None):
        return self._request('DELETE', path, data)
