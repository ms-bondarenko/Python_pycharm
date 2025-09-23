import requests
import pytest
from time import sleep

base_url = "https://ru.yougile.com"

bearer_token = "cokCA4XgOwc6fU4k8fOwmRXKuyHvzBE1aDIfObc61ZGmdvm91ea6ZMMwAm7Cw9Kb"
headers = {
        "Authorization": f"Bearer {bearer_token}",
        # "Authorization": "bearer_token",
        "Content-Type": "application/json"
    }

project_data = {
        "title": "Создание проекта",
        "users": {
            "20891e60-4009-430c-9f74-1f4435674303": "admin"
        }
    }

def get_project_list():
    resp = requests.get(base_url + '/api-v2/projects',headers=headers)
    return resp.json()


def test_list_project():
    body = get_project_list()
    list = len(body)
    assert len(body) > 0
    print(f"Количество проектов до добавления: {list}")

def test_add_new_project():
    body = get_project_list()
    list_before = len(body)
    print(f"Количество проектов до добавления: {list_before}")

    resp = requests.post(base_url + '/api-v2/projects', headers=headers, json=project_data)
    assert resp.status_code ==201

    sleep(10)

    body = get_project_list()
    list_after = len(body)
    assert list_before + 1 == list_after
