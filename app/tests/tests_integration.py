import unittest
import unittest.mock

from app.db import db
from app.main import app
from fastapi.testclient import TestClient


class IntegrationTests(unittest.TestCase):
    client = TestClient(app)

    def setUp(self) -> None:
        super().setUp()

        self.db = {'users': []}

    def test_register(self):
        with unittest.mock.patch.dict(db, self.db):
            response = self.client.get('/auth/list')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), [])

            self.client.post(
                '/auth/register',
                json={'name': 'Fang', 'password': 'pass'}
            )

            response = self.client.get('/auth/list')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(), [{'name': 'Fang', 'playlists': []}])

    def test_playlist_add(self):
        with unittest.mock.patch.dict(db, self.db):
            # Preparation
            # ----------------
            self.client.post(
                '/auth/register',
                json={'name': 'Fang', 'password': 'pass'}
            )
            # ----------------
            self.client.post('/playlist/add', json={
                'username': 'Fang',
                'name': 'p1',
                'songs': ['1', '2', '3']
            })
            response = self.client.get('/playlist/list?username=Fang')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), ['p1'])

    def test_songs_list(self):
        with unittest.mock.patch.dict(db, self.db):
            # Preparation
            # --------------------
            self.client.post(
                '/auth/register',
                json={'name': 'Fang', 'password': 'pass'}
            )
            self.client.post('/playlist/add', json={
                'username': 'Fang',
                'name': 'p1',
                'songs': ['1', '2', '3']
            })
            self.client.post('/playlist/add', json={
                'username': 'Fang',
                'name': 'p1',
                'songs': ['1', '3', '4']
            })
            # ---------------------
            response = self.client.get('/song/list?username=Fang')
            self.assertEqual(response.status_code, 200)
            self.assertSetEqual(set(response.json()), {'1', '2', '3', '4'})
