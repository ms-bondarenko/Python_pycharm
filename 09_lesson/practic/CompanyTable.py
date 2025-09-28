from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable:
    db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):
        return self.db.execute("select * from company").fetchall()

    def get_active_companies(self):
        return self.db.execute("select * from company where \"is_active\" = true").fetchall()

    def delete(self, id):
        sql = text("delete from company where id = :id_to_delete")
        self.db.execute(sql, id_to_delete = id)

