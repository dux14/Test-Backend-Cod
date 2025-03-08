import requests
from config import USER_ENDPOINT, DEFAULT_HEADERS

class UserAPI:
    def __init__(self):
        self.url = USER_ENDPOINT
        self.headers = DEFAULT_HEADERS
    
    def create_user(self, payload):
        """
        Performs a POST request to create a user.
        
        - If 'payload' is a dictionary, it's sent correctly as JSON.
        - If it's a string, it's assumed to be a malformed JSON to test negative scenarios.
        """
        if isinstance(payload, dict):
            response = requests.post(self.url, json=payload, headers=self.headers)
        else:
            response = requests.post(self.url, data=payload, headers=self.headers)
        return response
