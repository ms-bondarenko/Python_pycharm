import requests
import pytest

from config import base_url, token, ID_Project, ID_Project_negative

headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

@pytest.fixture
def change_project():
    return test_change_positive()

def test_change_positive():
    payload = {
        'title': 'TestWork123',
        'users': {
            '20891e60-4009-430c-9f74-1f4435674303': 'admin'
        }
    }

    resp = requests.put(f'{base_url}/api-v2/projects/{ID_Project}', json=payload, headers=headers)
    response_data = resp.json()
    assert 'id' in response_data
    assert resp.status_code == 200

def test_change_negative():
    payload = {
        'title': 'TestWork123',
        'users': {
            '20891e60-4009-430c-9f74-1f4435674303': 'admin'
        }
    }

    resp = requests.put(f'{base_url}/api-v2/projects/{ID_Project_negative}', json=payload, headers=headers)
    response_data = resp.json()
    # assert 'id' in response_data
    # assert resp.status_code == 401

    assert resp.status_code == 404
    assert response_data == {'error': 'Not Found', 'message': 'Проект не найден', 'statusCode': 404}