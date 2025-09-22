import requests
import pytest

from config import base_url, token, token_negative


@pytest.fixture
def create_project():
    return test_create_new_project_positive()

def test_create_new_project_positive():

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
    resp = requests.post(f'{base_url}/api-v2/projects', json=payload, headers=headers)
    response_data = resp.json()
    assert 'id' in response_data
    assert resp.status_code == 201


def test_create_new_project_negative():
    payload = {
        'title': '',
        'users': {
            '20891e60-4009-430c-9f74-1f4435674303': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
}
    resp = requests.post(f'{base_url}/api-v2/projects', json=payload, headers=headers)
    assert resp.status_code == 400

def test_create_new_project_negative():
    payload = {
        'title': 'Work',
        'users': {
            '20891e60-4009-430c-9f74-1f4435674303': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_negative}'
    }
    resp = requests.post(f'{base_url}/api-v2/projects', json=payload, headers=headers)
    response_data = resp.json()

    print(f'Ststus Code: {resp.status_code}')
    print(f'Response Data: {response_data}')
    assert resp.status_code == 401
    assert 'error' in response_data
    assert response_data['error'] == 'Unauthorized'




