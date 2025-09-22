import requests
import pytest

from config import base_url, token, projectID, projectID_neg

@pytest.fixture
def get_project():
    return test_get_positive()

def test_get_positive():
    payload = {
        'title': 'TestWork12',
        'users': {
            '20891e60-4009-430c-9f74-1f4435674303': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    resp = requests.get(f'{base_url}/api-v2/projects/{projectID}', json=payload, headers=headers)
    response_data = resp.json()
    assert 'id' in response_data
    assert resp.status_code == 200

def test_get_negative():
    payload = {
        'title': 'TestWork12',
        'users': {
            '20891e60-4009-430c-9f74-1f4435674303': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    resp = requests.get(f'{base_url}/api-v2/projects/{projectID_neg}', json=payload, headers=headers)
    response_data = resp.json()
    assert 'id' in response_data
    assert resp.status_code == 200