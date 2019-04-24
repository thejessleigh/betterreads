import json
from unittest import mock

import pytest

from betterreads.author import GoodreadsAuthor
from betterreads.book import GoodreadsBook
from betterreads.client import GoodreadsClient
from betterreads.user import GoodreadsUser


class TestAuthor:
    @pytest.fixture
    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_author(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")

        # Goodreads Author data pulled for Jeannette Ng on 2019-04-05. Lightly modified for testing purposes
        with open("tests/unit/fixtures/author.json") as f:
            author_response = f.read()
        mock_request.return_value = json.loads(author_response)
        return client.author(14880958)

    def test_get_author(self, test_author):
        assert isinstance(test_author, GoodreadsAuthor)
        assert test_author.gid == "14880958"
        assert repr(test_author) == "Jeannette Ng"

    def test_author_name(self, test_author):
        assert test_author.name == "Jeannette Ng"

    def test_author_about(self, test_author):
        assert test_author.about.startswith(
            "Jeannette Ng is originally from Hong Kong but now lives in Durham"
        )

    def test_author_books(self, test_author):
        books = test_author.books
        assert all(isinstance(book, GoodreadsBook) for book in books)
        titles = [book.title for book in books]
        assert "Under the Pendulum Sun" in titles

    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_author_with_one_book(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")

        # Goodreads Author data pulled for IACA on 2019-04-05. Lightly modified for testing purposes
        with open("tests/unit/fixtures/author_one_book.json") as f:
            author_response = f.read()
        mock_request.return_value = json.loads(author_response)
        books = client.author("5734084").books
        assert len(books) == 1

    def test_born_at(self, test_author):
        assert test_author.born_at == "1980/01/01"

    def test_died_at(self, test_author):
        assert test_author.died_at == "2018/12/31"

    def test_fans_count(self, test_author):
        assert test_author.fans_count == "149"

    def test_gender(self, test_author):
        assert test_author.gender == "test gender"

    def test_hometown(self, test_author):
        assert test_author.hometown == "test hometown"

    def test_link(self, test_author):
        assert (
            test_author.link
            == "https://www.goodreads.com/author/show/14880958.Jeannette_Ng"
        )

    def test_image_url(self, test_author):
        assert (
            test_author.image_url
            == "https://images.gr-assets.com/authors/1494425350p5/14880958.jpg"
        )

    def test_small_image_url(self, test_author):
        assert (
            test_author.small_image_url
            == "https://images.gr-assets.com/authors/1494425350p2/14880958.jpg"
        )

    def test_influences(self, test_author):
        assert test_author.influences is None

    def test_user(self, test_author):
        assert type(test_author.user) == GoodreadsUser

    def test_works_count(self, test_author):
        assert test_author.works_count == "5"
