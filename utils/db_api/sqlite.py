import sqlite3


class Database:
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
        CREATE TABLE Users (
            id int NOT NULL,
            name_user varchar(255) NOT NULL,
            task_1_writing str,
            name varchar(255),
            task_1_photo_id varchar(255),


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

    def add_user(self,
                 id: int,
                 name_user: str,
                 task_1_writing: str = None,
                 name: str = None,
                 task_1_photo_id: str = None

                 ):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name,) VALUES(1, 'John',)"

        sql = """
        INSERT INTO Users(id, name_user, task_1_writing, name, task_1_photo_id) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id,
                                      name_user,
                                      task_1_writing,
                                      name,
                                      task_1_photo_id
                                      ), commit=True)

    def update_task_1_photo_id(self, task_1_photo_id, id):

        sql = f"""
        UPDATE Users SET task_1_photo_id=? WHERE id=?
        """
        return self.execute(sql, parameters=(task_1_photo_id, id), commit=True)

    def update_user_self_info(self, self_info, id):

        sql = f"""
        UPDATE Users SET self_info=? WHERE id=?
        """
        return self.execute(sql, parameters=(self_info, id), commit=True)

    def update_name(self, name, id):
        # SQL_EXAMPLE = "UPDATE Users SET name=name WHERE id=12345"

        sql = f"""
        UPDATE Users SET name=? WHERE id=?
        """
        return self.execute(sql, parameters=(name, id), commit=True)

    def update_task_1_writing(self, task_1_writing, id):

        sql = f"""
        UPDATE Users SET task_1_writing=? WHERE id=?
        """
        return self.execute(sql, parameters=(task_1_writing, id), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self):
        self.execute("""DELETE FROM Users WHERE TRUE""", commit=True)

    def select_from_table(self):
        sql = """
        SELECT id FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_name(self):
        sql = """
        SELECT name_user FROM Users
        """
        return self.execute(sql, fetchall=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
