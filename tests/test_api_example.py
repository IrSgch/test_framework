
import requests

def test_example_api_status_code():
    response = requests.get("https://example.com")
    assert response.status_code == 200

def test_example_api_headers():
    response = requests.get("https://example.com")
    assert "text/html" in response.headers["Content-Type"]


