from companyApi import companyApi
from CompanyTable import CompanyTable

api = companyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    assert  len(api_result) == len(db_result)


def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={'active':'true'})
    db_list = db.get_active_companies()
    assert len(db_list) == len(filtered_list)

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    result = api.create_company("прикол", "зачет")
    new_id = result["id"]


    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before ==1
    found = True
    for company in body:
        if "id" in company:  # Проверяем наличие ключа 'id'
            if company["id"] == new_id:
                assert company["name"] == "прикол"  # Проверяем имя компании
                found = True
                break

    assert found, f"Компания с ID {new_id} не найдена в списке. Полученный список: {body}"
    # for company in body:
    #     if company["id"] == new_id:
    #         assert company["name"] == "прикол"
    #         assert company["description"] == "зачет"
    #         assert company["id"] == new_id
    db.delete(new_id)



