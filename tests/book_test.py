import json
from unittest import mock

import pytest

from betterreads.author import GoodreadsAuthor
from betterreads.book import GoodreadsBook
from betterreads.client import GoodreadsClient


class TestBook:
    @pytest.fixture
    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_book(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")
        with open("tests/fixtures/book.json") as f:
            book_response = f.read()
            mock_request.return_value = json.loads(book_response)
        return client.book(39721925)

    def test_get_book(self, test_book):
        assert isinstance(test_book, GoodreadsBook)
        assert test_book.gid == "39721925"
        assert (
            repr(test_book)
            == "The Personality Brokers: The Strange History of Myers-Briggs and the Birth of Personality Testing"
        )

    def test_title(self, test_book):
        assert (
            test_book.title
            == "The Personality Brokers: The Strange History of Myers-Briggs and the Birth of Personality Testing"
        )

    def test_authors(self, test_book):
        assert len(test_book.authors) == 1
        assert isinstance(test_book.authors[0], GoodreadsAuthor)

    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_many_authors(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")

        # Goodreads Book data - Practical Data Science with R as of 2019-04-05. Lightly modified for testing purposes.
        with open("tests/fixtures/book_multiple_authors.json") as f:
            book_response = f.read()
        mock_request.return_value = json.loads(book_response)

        book = client.book("18774683")
        assert len(book.authors) == 2
        assert isinstance(book.authors[0], GoodreadsAuthor)

    def test_description(self, test_book):
        assert test_book.description.startswith(
            "An unprecedented history of the personality test conceived a century ago"
        )

    def test_average_rating(self, test_book):
        rating = float(test_book.average_rating)
        assert type(rating) == float
        assert rating == 3.38

    def test_rating_dist(self, test_book):
        assert test_book.rating_dist.startswith("5:")

    def test_ratings_count(self, test_book):
        assert test_book.ratings_count == "935"

    def test_text_reviews_count(self, test_book):
        assert test_book.text_reviews_count == "195"

    def test_num_pages(self, test_book):
        assert test_book.num_pages == "307"

    def test_popular_shelves(self, test_book):
        shelf_names = [shelf.get("@name") for shelf in test_book.popular_shelves]
        assert "to-read" in shelf_names
        assert all(isinstance(shelf, dict) for shelf in test_book.popular_shelves)

    def test_work(self, test_book):
        assert type(test_book.work) == dict
        assert test_book.work["id"]["#text"] == "60781039"

    def test_series_works(self, test_book):
        assert test_book.series_works is None

    # TODO: Add test book with series works

    def test_publication_date(self, test_book):
        assert test_book.publication_date == ("9", "11", "2018")

    def test_publisher(self, test_book):
        assert test_book.publisher == "Doubleday"

    def test_language_code(self, test_book):
        assert test_book.language_code == "eng"

    def test_edition_information(self, test_book):
        assert test_book.edition_information is None

    # TODO: Add test book with edition information

    def test_image_url(self, test_book):
        assert (
            test_book.image_url
            == "https://images.gr-assets.com/books/1522909584m/39721925.jpg"
        )

    def test_small_image_url(self, test_book):
        assert (
            test_book.small_image_url
            == "https://images.gr-assets.com/books/1522909584s/39721925.jpg"
        )

    def test_is_ebook(self, test_book):
        assert test_book.is_ebook == "false"

    def test_format(self, test_book):
        assert test_book.format == "Hardcover"

    def test_isbn(self, test_book):
        assert test_book.isbn == "0385541902"

    def test_isbn13(self, test_book):
        assert test_book.isbn13 == "9780385541909"

    def test_link(self, test_book):
        assert (
            test_book.link
            == "https://www.goodreads.com/book/show/39721925-the-personality-brokers"
        )

    def test_reviews_widget(self, test_book):
        assert test_book.reviews_widget.startswith("<style>")
        assert test_book.reviews_widget.endswith("</div>")

    def test_similar_books(self, test_book):
        assert all(isinstance(b, GoodreadsBook) for b in test_book.similar_books)
