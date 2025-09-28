import pytest
from sqlalchemy import create_engine,text
from config import user,passwword, db, host, port

db_connection_string = f"postgresql://{user}:{passwword}@{host}:{port}/{db}"
engine = create_engine(db_connection_string)

def test_db_connection():
    connect = create_engine(db_connection_string)
    names = connect.table_names()
    assert names[0] == 'users'

def test_select():
    connect = create_engine(db_connection_string)
    rows = connect.execute("select * from users").fetchall()
    row1 = rows[0]
    expected = 42568

    assert row1["user_id"] == expected

def test_create_users():
    connect = create_engine(db_connection_string)
    max_id = connect.execute("SELECT MAX(user_id) AS max_user_id FROM users").scalar()

    new_user_id = max_id+1
    sql = text("INSERT INTO users (user_id, user_email, subject_id ) VALUES (:user_id, :user_email, :subject_id)")
    connect.execute(sql, {"user_id": new_user_id, "user_email": "table@table.ru", "subject_id": 2})

    max_id1 = connect.execute("SELECT MAX(user_id) AS max_user_id FROM users").scalar()

    assert max_id+1 == max_id1

def test_update_users():
    connect = create_engine(db_connection_string)
    sql = text("UPDATE users SET subject_id = :subject WHERE user_email = 'table@table.ru'")
    connect.execute(sql, {"subject": 4,})

    updated_subject_id = connect.execute("SELECT subject_id FROM users WHERE user_email = 'table@table.ru'").scalar()

    assert  updated_subject_id == 4

def test_delete_users():
    connect = create_engine(db_connection_string)
    delet = text("delete from users where user_email = 'table@table.ru'")
    connect.execute(delet)

    count = text("SELECT COUNT(*) FROM users WHERE user_email = 'table@table.ru'")
    result = connect.execute(count).scalar()

    assert result == 0


