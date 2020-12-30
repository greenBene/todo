import unittest
import os

import Item
import User


class ItemCase(unittest.TestCase):
    database_path = 'test.db'
    user_name = 'Test User'

    def setUp(self):
        if os.path.exists(self.database_path):
            os.remove(self.database_path)

        self.item_session = Item.Item(self.database_path)
        self.user_session = User.User(self.database_path)
        self.user_id = self.user_session.create(user_name=self.user_name)

    def test_create_item(self):
        item_name = 'Test Todo'
        item_id = self.item_session.create(user_id=self.user_id, item_name=item_name)
        self.assertTrue(self.item_session.exists(user_id=self.user_id, item_id=item_id))

    def test_get_item_list(self):
        for i in range(5):
            self.item_session.create(user_id=self.user_id, item_name=f"Test Item {i}")

        items = self.item_session.get_items(user_id=self.user_id)
        self.assertEqual(len(items), 5)

    def test_delete_item(self):
        item_name = 'Item To Delete'
        item_id = self.item_session.create(user_id=self.user_id, item_name=item_name)
        self.item_session.delete(item_id)
        self.assertFalse(self.item_session.exists(user_id=self.user_id, item_id=item_id))
