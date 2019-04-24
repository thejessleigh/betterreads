"""Client is the primary interface for interacting with the Goodreads API. This integration test makes live API
calls and affirms that the correct objects are being returned. For a more comprehensive test that each of the interface
objects is created and functions properly when given the correct inputs, check the unit test suite."""
import os

import pytest

from betterreads.author import GoodreadsAuthor
from betterreads.book import GoodreadsBook
from betterreads.client import GoodreadsClient, GoodreadsClientException
from betterreads.comment import GoodreadsComment
from betterreads.event import GoodreadsEvent
from betterreads.group import GoodreadsGroup
from betterreads.review import GoodreadsReview


class TestClient:
    @pytest.fixture
    def test_client_fixture(self):
        return GoodreadsClient(
            os.environ.get("GOODREADS_KEY"), os.environ.get("GOODREADS_SECRET")
        )

    def test_auth_user_no_session(self, test_client_fixture):
        with pytest.raises(GoodreadsClientException):
            test_client_fixture.auth_user()

    def test_author_by_id(self, test_client_fixture):
        author = test_client_fixture.author(8566992)
        assert isinstance(author, GoodreadsAuthor)

    def test_author_by_name(self, test_client_fixture):
        author = test_client_fixture.find_author("Stephen King")
        assert isinstance(author, GoodreadsAuthor)

    def test_book_by_id(self, test_client_fixture):
        book = test_client_fixture.book(123455)
        assert isinstance(book, GoodreadsBook)

    def test_search_books(self, test_client_fixture):
        books = test_client_fixture.search_books(
            q="Daniel Mallory Ortberg", search_field="author"
        )
        assert len(books) > 1
        assert all(isinstance(book, GoodreadsBook) for book in books)

    def test_book_no_options_given(self, test_client_fixture):
        with pytest.raises(GoodreadsClientException):
            test_client_fixture.book(None, None)

    def test_search_books_with_one_book(self, test_client_fixture):
        books = test_client_fixture.search_books(
            "Childhood, Boyhood, Truth: From an African Youth to the Selfish Gene"
        )
        assert len(books) == 1
        assert all(isinstance(book, GoodreadsBook) for book in books)

    def test_group_by_id(self, test_client_fixture):
        group = test_client_fixture.group(1)
        assert isinstance(group, GoodreadsGroup)

    def test_find_groups(self, test_client_fixture):
        groups = test_client_fixture.find_groups("Goodreads Developers")
        assert len(groups) > 1
        assert all(isinstance(group, GoodreadsGroup) for group in groups)

    def test_list_events(self, test_client_fixture):
        events = test_client_fixture.list_events(80126)
        assert len(events) > 0
        assert all(isinstance(event, GoodreadsEvent) for event in events)

    def test_search_books_total_pages(self, test_client_fixture):
        num_pages = test_client_fixture.search_books_total_pages(
            q="Joe Hill", search_field="author"
        )
        assert isinstance(num_pages, int)

    def test_search_books_all_pages(self, test_client_fixture):
        books = test_client_fixture.search_books_all_pages(
            q="Daniel Jose Older", search_field="author"
        )
        assert len(books) > 10
        assert all(isinstance(book, GoodreadsBook) for book in books)

    def test_get_review(self, test_client_fixture):
        review = test_client_fixture.review(12345)
        assert isinstance(review, GoodreadsReview)

    def test_list_comments_review(self, test_client_fixture):
        comments = test_client_fixture.list_comments("review", 1618778364)
        assert all(isinstance(comment, GoodreadsComment) for comment in comments)

    def test_get_recent_reviews(self, test_client_fixture):
        reviews = test_client_fixture.recent_reviews()
        assert all(isinstance(review, GoodreadsReview) for review in reviews)
