import pytest
from pages.user_api import UserAPI
from config import STATUS_CREATED, STATUS_BAD_REQUEST

@pytest.mark.parametrize("payload, expected_status, expected_data", [
    (
        {"name": "John Arias", "job": "Software Engineer"}, 
        STATUS_CREATED, 
        {"name": "John Arias", "job": "Software Engineer"}
    ),
    (
        {"name": "John Arias", "job": "Software Engineer", "gender": "Male", "age": 33}, 
        STATUS_CREATED, 
        {"name": "John Arias", "job": "Software Engineer", "gender": "Male", "age": 33}
    ),
])
def test_create_user_positive(payload, expected_status, expected_data):
    user_api = UserAPI()
    response = user_api.create_user(payload)
    
    assert response.status_code == expected_status
    
    json_response = response.json()
    for key, value in expected_data.items():
        assert json_response[key] == value

    assert json_response.get("id") is not None
    assert json_response.get("createdAt") is not None
    
    if "age" in expected_data:
        assert isinstance(json_response["age"], int)

def test_create_user_negative():
    malformed_json = '{"name": "Daniel Bernal", "job": "Automation Test", "gender": "Male", "age": 33, }'
    user_api = UserAPI()
    response = user_api.create_user(malformed_json)
    assert response.status_code == STATUS_BAD_REQUEST
