import unittest
import os

from User import User


class TestUser(unittest.TestCase):
    database_path = 'test.db'

    def setUp(self):
        if os.path.exists(self.database_path):
            os.remove(self.database_path)
        self.user_session = User(self.database_path)

    def test_create_new_user(self):
        name = 'Test User'
        user_id = self.user_session.create(user_name=name)
        self.assertTrue(self.user_session.exists(user_id=user_id))

    def test_user_exists_fails(self):
        user_id = -1
        self.assertFalse(self.user_session.exists(user_id=user_id))

    def test_delete_user(self):
        user_name = 'User To Delete'
        user_id = self.user_session.create(user_name=user_name)
        self.user_session.delete(user_id=user_id)
        self.assertFalse(self.user_session.exists(user_id=user_id))
