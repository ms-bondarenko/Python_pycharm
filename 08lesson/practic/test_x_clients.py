from companyApi import companyApi

api = companyApi("http://5.101.50.27:8000")

def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0

def test_get_active_companies():
    full_list = api.get_company_list()

    filtered_list = api.get_company_list(params_to_add={'active':'true'})

    assert len(full_list) > len(filtered_list)

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    result = api.create_company("прикол", "зачет")
    new_id = result["id"]


    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before ==1
    assert  body[-1]["name"] == "прикол"
    assert  body[-1]["description"] == "зачет"


