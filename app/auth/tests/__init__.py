import unittest
import unittest.mock

import app.auth.router as router
from app.auth.types import User
from app.db import db
from app.types.user import User as UserModel


class TestAuth(unittest.TestCase):
    test_user = UserModel('Fang', [])

    def test_register(self):
        with unittest.mock.patch.dict(db, {'users': []}):
            router.register(User(name='Fang', password='pass'))
            self.assertEqual(db['users'], [self.test_user])

    def test_get(self):
        with unittest.mock.patch.dict(db, {'users': [self.test_user]}):
            res = router.list()
            self.assertEqual(res, [self.test_user])

    def test_register_twice(self):
        with unittest.mock.patch.dict(db, {'users': []}):
            router.register(User(name='Fang', password='pass'))
            router.register(User(name='Fang', password='pass2'))
            self.assertEqual(db['users'], [self.test_user])
