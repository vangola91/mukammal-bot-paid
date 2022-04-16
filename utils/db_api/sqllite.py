import sqlite3

class Databaes:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users(
        id int NOT NULL, 
        Name varcher(255) NOT NULL,
        email varchar (255),
        phone varcher(20),
        PRIMARY KEY (id)
        );
"""
        self.execute(sql, commit=True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, phone: str = None):


        sql = """
        INSERT INTO Users(id, Name, email, phone) VALUES(?, ?, ?, ?)       
        """
        self.execute(sql, parameters=(id, name, email, phone), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)


    def select_users(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    #User son olish
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)
    #user email yangilash
    def update_users_email(self, email, id):

        sql = f"""
        UPDATE Users SET email=? WHERE  id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def update_users_phone(self, phone, id):

        sql = f"""
        UPDATE Users SET phone=? WHERE  id=?
        """
        return self.execute(sql, parameters=(phone, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
    _________________________________________________
    Executing:
    {statement}
    __________________________________________________
    """)