import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/700')
    assert response.status_code == 200

def test_body_text():
    response = requests.get('https://petstore.swagger.io/v2/pet/700')
    assert response.json()['name'] == 'neko'
