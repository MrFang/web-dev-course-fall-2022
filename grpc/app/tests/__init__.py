from typing import Dict, List, Tuple
import unittest
from app.utils import get_files_with_content
import os
import shutil
from parameterized import parameterized


class TestUtils(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.content_root = os.path.join(dir_path, 'content-root')

    def setUp(self) -> None:
        super().setUp()
        os.makedirs(self.content_root, exist_ok=True)

    def tearDown(self) -> None:
        super().tearDown()
        shutil.rmtree(self.content_root)

    def create_files(self, files_with_content: List[Tuple[str, bytes]]):
        for name, content in files_with_content:
            dir = os.path.dirname(name)

            if dir != '':
                os.makedirs(os.path.join(self.content_root, dir))

            with open(os.path.join(self.content_root, name), 'wb') as f:
                f.write(content)

    @parameterized.expand([
        (
            [('foo.txt', b'foo'), ('bar.txt', b'bar')],
            {'foo.txt': b'foo', 'bar.txt': b'bar'}
        ),
        ([('foo/bar.txt', b'bar'), ('baz.txt', b'baz')], {'baz.txt': b'baz'}),
    ])
    def test_get_files_from_dir(
        self,
        files_with_content: List[Tuple[str, bytes]],
        expected: Dict[str, bytes]
    ):
        self.create_files(files_with_content)
        res = get_files_with_content(self.content_root)
        self.assertDictEqual(expected, res)

    def test_get_single_file(self):
        self.create_files([('foo.txt', b'foo'), ('bar.txt', b'bar')])
        res = get_files_with_content(
            os.path.join(self.content_root, 'foo.txt'))
        self.assertDictEqual({'foo.txt': b'foo'}, res)

    def test_not_exists(self):
        res = get_files_with_content(
            os.path.join(self.content_root, 'not-exists'))
        self.assertDictEqual({}, res)
