import json
from unittest import mock

import pytest

from betterreads.client import GoodreadsClient
from betterreads.review import GoodreadsReview


class TestReview:
    @pytest.fixture
    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_review(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")

        # Goodreads Group data pulled on 2019-04-09. Lightly modified for testing purposes
        with open("tests/unit/fixtures/review.json") as f:
            review_response = f.read()
            mock_request.return_value = json.loads(review_response)
        return client.review(12345)

    def test_repr(self, test_review):
        assert repr(test_review) == "review [12345]"

    def test_review_gid(self, test_review):
        assert test_review.gid == "12345"

    def test_review_book(self, test_review):
        assert test_review.book["isbn"] == "0316767727"

    def test_review_rating(self, test_review):
        assert test_review.rating == "5"

    def test_review_shelves(self, test_review):
        assert len(test_review.shelves) == 1

    def test_review_recommended_for(self, test_review):
        assert test_review.recommended_for is None

    def test_review_recommended_by(self, test_review):
        assert test_review.recommended_by is None

    def test_review_started_at(self, test_review):
        assert test_review.started_at == "Thu Aug 31 00:00:00 -0700 2000"

    def test_review_read_at(self, test_review):
        assert test_review.read_at == "Fri Sep 01 00:00:00 -0700 2000"

    def test_review_body(self, test_review):
        assert test_review.body == "These are some words in the review body"

    def test_review_comments_count(self, test_review):
        assert test_review.comments_count == "0"

    def test_review_url(self, test_review):
        assert test_review.url == "https://www.goodreads.com/review/show/12345"

    def test_review_owned(self, test_review):
        assert test_review.owned == "0"
