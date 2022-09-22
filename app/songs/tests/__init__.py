import unittest
import unittest.mock
from typing import Set

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
                ),
                User(
                    'With-Similar',
                    [
                        Playlist('fst', ['s1']),
                        Playlist('snd', ['s1', 's2']),
                        Playlist('trd', ['s1', 's3'])
                    ]
                )
            ]
        }

    @parameterized.expand([
        ('Fang', {'p1_s1', 'p1_s2', 'p2_s1', 'p2_s2'}),
        ('Not-exists', set()),
        ('With-Similar', {'s1', 's2', 's3'})
    ])
    def test_user_playlists(self, username: str, expected_songs: Set[str]):
        with unittest.mock.patch.dict(db, self.db):
            res = router.get_user_songs(username)

            for s in expected_songs:
                self.assertIn(s, res)
