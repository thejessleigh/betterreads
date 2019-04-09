import json
from unittest import mock, skip

import pytest

from betterreads.client import GoodreadsClient
from betterreads.group import GoodreadsGroup
from betterreads.owned_book import GoodreadsOwnedBook
from betterreads.review import GoodreadsReview
from betterreads.shelf import GoodreadsShelf
from betterreads.user import GoodreadsUser


class TestUser:
    @pytest.fixture
    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_user(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")
        # User data for test user fetched 2019-04-09. Lightly modified for testing purposes
        with open("tests/fixtures/user.json") as f:
            user_response = f.read()
            mock_request.return_value = json.loads(user_response)
        return client.user(95040664)

    def test_repr(self, test_user):
        assert repr(test_user) == "mitzynitzy"

    def test_get_user(self, test_user):
        assert isinstance(test_user, GoodreadsUser)
        assert test_user.gid == "95040664"

    def test_user_name(self, test_user):
        assert test_user.user_name == "mitzynitzy"

    def test_name(self, test_user):
        assert test_user.name == "Mitzy Nitzy"

    def test_link(self, test_user):
        assert (
            test_user.link == "https://www.goodreads.com/user/show/95040664-mitzy-nitzy"
        )

    def test_image_urls(self, test_user):
        assert (
            test_user.image_url
            == "https://images.gr-assets.com/users/1554823256p3/95040664.jpg"
        )
        assert (
            test_user.small_image_url
            == "https://images.gr-assets.com/users/1554823256p2/95040664.jpg"
        )

    @skip("Makes live call - come back to this after groups tests are done")
    def test_user_not_in_groups(self, test_user):
        groups = test_user.list_groups()
        assert isinstance(groups, list)
        assert len(test_user.list_groups()) == 0

    @skip("Makes live call - come back to this after groups tests are done")
    def test_user_in_groups(self, test_user):
        groups = test_user.list_groups()
        assert all(isinstance(group, GoodreadsGroup) for group in groups)

    @skip("Makes live call - come back to this after owned_books tests are done")
    def test_user_own_books(self):
        owned_books = self.user.owned_books()
        print(owned_books)
        ok_(all(isinstance(book, GoodreadsOwnedBook) for book in owned_books))

    @skip("Makes live call - come back to this after reviews tests are done")
    def test_reviews(self):
        reviews = self.user.reviews()
        ok_(all(isinstance(review, GoodreadsReview) for review in reviews))

    @skip("Makes live call - come back to this after shelves tests are done")
    def test_shelves(self):
        shelves = self.user.shelves()
        ok_(all(isinstance(shelf, GoodreadsShelf) for shelf in shelves))

    @skip("Function new to this version - test later.")
    def test_per_shelf_reivews(self):
        pass
