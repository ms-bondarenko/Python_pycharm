from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgres://qa:skyqa@5.101.50.27:5432/x_clients"

db = create_engine(db_connection_string)

def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert  names[7] == 'company'
    print(names)

def test_select():
    db =create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")

    rows = db.execute(sql_statement, company_id = 5).fetchall()
    assert len(rows) == 1
    assert rows[0] ["name"] == "Служба поддержки QA"


def test_select_1():
    db =create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[-1]

    assert row1[0] == 89
    assert row1["name"] == "The Best Company"
    assert row1["description"] == "Best Company"

def test_select_row_two_filter():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"is_active\" = :is_active and  id >= :id")

    my_params = {
        'id':6,
        'is_active': True
    }
    rows = db.execute(sql_statement, my_params).fetchall()
    assert len(rows) == 76

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:new_name)")

    rows =db.execute(sql, new_name = 'QA Work')

def test_update():
    db = create_engine(db_connection_string)
    sql = text("UPDATE company SET description = :descr WHERE id = :id")

    db.execute(sql, descr = "WorkSpase", id =90)

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    db.execute(sql, id = 90)




