import unittest
import unittest.mock
from typing import List, Optional

import app.playlist.router as router
from app.db import db
from app.types.playlist import Playlist as PlaylistModel
from app.types.user import User
from parameterized import parameterized
from app.playlist.types import Playlist


class TestPlaylist(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.db = {
            'users': [
                User(
                    'Fang',
                    [
                        PlaylistModel('first', ['p1_s1', 'p1_s2']),
                        PlaylistModel('second', ['p2_s1', 'p2_s2'])
                    ]
                )
            ]
        }

    @parameterized.expand([('Fang', ['first', 'second']), ('Not-exists', [])])
    def test_user_playlists(self, username: str, expected_names: List[str]):
        with unittest.mock.patch.dict(db, self.db):
            res = router.user_playlists(username)
            self.assertEqual(res, expected_names)

    def test_add_playlist(self):
        with unittest.mock.patch.dict(db, self.db):
            router.add_playlist(Playlist(
                username='Fang',
                name='third',
                songs=['p3_s1', 'p3_s2']
            ))
            self.assertEqual(len(db['users'][0].playlists), 3)

            created: Optional[PlaylistModel] = next(
                (p for p in db['users'][0].playlists if p.name == 'third'),
                None
            )
            self.assertIsNotNone(created)
            self.assertEqual(created.songs, ['p3_s1', 'p3_s2'])
