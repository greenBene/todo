import sqlite3


class Item:
    database_table_creation_sql = \
        '''
        CREATE TABLE items (
            item_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT NOT NULL,
            
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        '''

    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.connection.execute(self.database_table_creation_sql)
        self.connection.commit()

    def create(self, user_id, item_name):
        item_creation_sql = f'INSERT INTO items(user_id, name) VALUES ({user_id}, \'{item_name}\')'
        self.connection.execute(item_creation_sql)
        self.connection.commit()
        item_id = self.get_item_id(user_id=user_id, item_name=item_name)
        return item_id

    def get_item_id(self, user_id, item_name):
        user_get_id_sql = f'SELECT item_id FROM items WHERE name =\'{item_name}\''
        result = self.connection.execute(user_get_id_sql)
        user_id = result.fetchone()[0]
        return user_id

    def get_items(self, user_id):
        item_collection_sql = f'SELECT item_id, name FROM items WHERE user_id = {user_id}'
        result = self.connection.execute(item_collection_sql)
        items = result.fetchall()
        return items

    def exists(self, user_id, item_id):
        items = self.get_items(user_id=user_id)

        if item_id in [i[0] for i in items]:
            return True
        else:
            return False

    def delete(self, item_id):
        item_deletion_sql = f'DELETE FROM items WHERE item_id = {item_id}'
        self.connection.execute(item_deletion_sql)