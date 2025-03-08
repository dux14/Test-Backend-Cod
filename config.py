"""
Configuration file for API testing.
Contains all the constants and configuration variables used in the tests.
"""

# API Configuration
API_BASE_URL = "https://reqres.in/api"
USER_ENDPOINT = f"{API_BASE_URL}/users"

# Headers
DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}

# HTTP Status Codes
STATUS_CREATED = 201
STATUS_BAD_REQUEST = 400 