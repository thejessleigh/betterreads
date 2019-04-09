import json
from unittest import mock, skip

import pytest

from betterreads.book import GoodreadsBook
from betterreads.client import GoodreadsClient
from betterreads.owned_book import GoodreadsOwnedBook
from betterreads.review import GoodreadsReview


class TestOwnedBook:
    @pytest.fixture
    def test_owned_book(self):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")
        with mock.patch("betterreads.client.GoodreadsSession") as mock_session:
            client.session = mock_session
            with open("tests/fixtures/owned_book.json") as f:
                owned_book_response = f.read()
                client.session.get.return_value = json.loads(owned_book_response)
            return client.owned_book(49488032)

    @pytest.fixture
    def test_owned_book_missing_original_data(self):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")
        with mock.patch("betterreads.client.GoodreadsSession") as mock_session:
            client.session = mock_session
            with open("tests/fixtures/owned_book_missing_original_data.json") as f:
                owned_book_response = f.read()
                client.session.get.return_value = json.loads(owned_book_response)
            return client.owned_book(6133754)

    def test_owned_book_instantiated(self, test_owned_book):
        assert isinstance(test_owned_book, GoodreadsOwnedBook)
        assert test_owned_book.gid == "49488032"

    def test_book(self, test_owned_book):
        assert isinstance(test_owned_book.book, GoodreadsBook)
        assert test_owned_book.book.title == "Her Body and Other Parties"

    def test_review(self, test_owned_book):
        assert isinstance(test_owned_book.review, GoodreadsReview)
        assert test_owned_book.review.gid == "2163802700"

    def test_current_owner(self, test_owned_book):
        assert test_owned_book.current_owner == "1724077"

    def test_original_purchase_date(self, test_owned_book):
        assert test_owned_book.original_purchase_date == "2017-12-25T08:00:00+00:00"

    def test_without_original_purchase_date(
        self, test_owned_book_missing_original_data
    ):
        assert test_owned_book_missing_original_data.original_purchase_date is None

    def test_original_purchase_location(self, test_owned_book):
        assert test_owned_book.original_purchase_location == "Gift from Sabrina"

    def test_without_original_purchase_location(
        self, test_owned_book_missing_original_data
    ):
        assert test_owned_book_missing_original_data.original_purchase_location is None

    def test_condition(self, test_owned_book):
        assert test_owned_book.condition == "Brand new"

    def test_link(self, test_owned_book):
        assert test_owned_book.link == "https://www.goodreads.com/owned_books/49488032"
