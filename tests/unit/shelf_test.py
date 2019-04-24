import json

import pytest

from betterreads.user_shelf import GoodreadsUserShelf


class TestUserShelf:
    @pytest.fixture
    def test_shelf(self):
        with open("tests/unit/fixtures/shelf.json") as f:
            shelf_dict = f.read()
            return GoodreadsUserShelf(json.loads(shelf_dict))

    def test_shelf_repr(self, test_shelf):
        assert repr(test_shelf) == "read"

    def test_shelf_name(self, test_shelf):
        assert test_shelf.name == "read"

    def test_shelf_book_count(self, test_shelf):
        assert test_shelf.count == "3"

    def test_shelf_exclusive_flag(self, test_shelf):
        assert test_shelf.exclusive == "true"

    def test_shelf_description(self, test_shelf):
        assert test_shelf.description is None

    def test_shelf_gid(self, test_shelf):
        assert test_shelf.gid == "308827957"

    def test_shelf_sticky(self, test_shelf):
        assert test_shelf.sticky is None

    def test_shelf_featured(self, test_shelf):
        assert test_shelf.featured == "true"
