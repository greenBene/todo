import sqlite3


class User:
    database_table_creation_sql = \
        '''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY, 
            name TEXT UNIQUE NOT NULL
        )
        '''

    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.connection.execute(self.database_table_creation_sql)
        self.connection.commit()

    def create(self, user_name):
        user_creation_sql = f'INSERT INTO users(name) VALUES (\'{user_name}\')'
        self.connection.execute(user_creation_sql)
        self.connection.commit()
        user_id = self.get_user_id(user_name=user_name)
        return user_id

    def delete(self, user_id):
        user_deletion_sql = f'DELETE FROM users WHERE user_id={user_id}'
        self.connection.execute(user_deletion_sql)
        self.connection.commit()

    def exists(self, user_id):
        user_exists_sql = f'SELECT COUNT(*) FROM users WHERE user_id = \'{user_id}\''
        result = self.connection.execute(user_exists_sql)
        user_count = result.fetchone()[0]
        if user_count >= 1:
            return True
        else:
            return False

    def get_user_id(self, user_name):
        user_get_id_sql = f'SELECT user_id FROM users WHERE name =\'{user_name}\''
        result = self.connection.execute(user_get_id_sql)
        user_id = result.fetchone()[0]
        return user_id

