import requests

base_url = "http://5.101.50.27:8000"

def test_simple_req():
    resp = requests.get(base_url+'/company/list')

    response_body = resp.json()
    first_company = response_body[0]
    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

def test_auth():

    creds = {
        'username' : 'harrypotter',
        'password' : 'expelliarmus'
    }

    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["user_token"]
    assert resp.status_code == 200
    print(resp.status_code)
    print(resp.json())

def test_create_company():
    company = {
        "name": "Армавир",
        "description": "Запросы"
    }
    resp = requests.post(base_url+'/company/create', json=company)
    print("Status Code:", resp.status_code)
    print("Response JSON:", resp.json())
    assert resp.status_code == 201

def test_get_companies():
    resp = requests.get(base_url+'/company/list')
    body = resp.json()
    print(body)

    assert resp.status_code == 200
    assert len(body) > 0

def test_simple_reqs():
    resp = requests.get(base_url+'/company/list')
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) >0

