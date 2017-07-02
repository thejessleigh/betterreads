from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.review import GoodreadsReview
from nose.tools import eq_, ok_

class TestReview():
    @classmethod
    def setup_class(cls):
        cls.client = GoodreadsClient(apikey.key, apikey.secret)
        cls.client.authenticate(apikey.oauth_access_token,
                                apikey.oauth_access_token_secret)
        cls.review = cls.client.review('2')

    def test_recent_reviews(self):
        reviews = self.client.recent_reviews()
        ok_(all(isinstance(r, GoodreadsReview) for r in reviews))

    def test_review_gid(self):
        eq_(self.review.gid, '2')

    def test_review_book(self):
        eq_(self.review.book['isbn'], '0517226952')

    def test_review_rating(self):
        eq_(self.review.rating, '5')

    def test_review_shelves(self):
        eq_(len(self.review.shelves), 6)

    def test_review_recommended_for(self):
        eq_(self.review.recommended_for, None)

    def test_review_recommended_by(self):
        eq_(self.review.recommended_by, 'Keaka')

    def test_review_started_at(self):
        eq_(self.review.started_at, None)

    def test_review_read_at(self):
        eq_(self.review.read_at, None)

    def test_review_body(self):
        eq_(self.review.body, None)

    def test_review_comments_count(self):
        eq_(self.review.comments_count, '0')

    def test_review_url(self):
        eq_(self.review.url, 'https://www.goodreads.com/review/show/2')

    def test_review_owned(self):
        eq_(self.review.owned, '1')
