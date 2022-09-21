import unittest
import unittest.mock
from typing import List

import app.songs.router as router
from app.db import db
from app.types.playlist import Playlist
from app.types.user import User
from parameterized import parameterized


class TestSongs(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.db = {
            'users': [
                User(
                    'Fang',
                    [
                        Playlist('first', ['p1_s1', 'p1_s2']),
                        Playlist('second', ['p2_s1', 'p2_s2'])
                    ]
                )
            ]
        }

    @parameterized.expand([
        ('Fang', ['p1_s1', 'p1_s2', 'p2_s1', 'p2_s2']),
        ('Not-exists', [])
    ])
    def test_user_playlists(self, username: str, expected_songs: List[str]):
        with unittest.mock.patch.dict(db, self.db):
            res = router.get_user_songs(username)
            self.assertEqual(res, expected_songs)
