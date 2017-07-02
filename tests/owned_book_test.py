from nose.tools import eq_, ok_

from goodreads import apikey
from goodreads.client import GoodreadsClient


class TestOwnedBook():
    @classmethod
    def setup_class(cls):
        cls.client = GoodreadsClient(apikey.key, apikey.secret)
        cls.client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.owned_book = cls.client.owned_book('43018920')

    def test_owned_book(self):
        eq_(self.owned_book.gid, '43018920')

    def test_book(self):
    	eq_(self.owned_book.book.title,'Cosmos')

    def test_review(self):
    	eq_(self.owned_book.review.gid,'437219861')

    def test_current_owner(self):
    	eq_(self.owned_book.current_owner,'6205894')

    def test_original_purchase_date(self):
    	book = self.client.owned_book('47481789')
    	eq_(book.original_purchase_date,'2015-03-09T07:00:00+00:00')

    def test_without_original_purchase_date(self):
    	eq_(self.owned_book.original_purchase_date,'')

    def test_original_purchase_location(self):
    	book = self.client.owned_book('47481789')
    	eq_(book.original_purchase_location,'Brazil')

    def test_without_original_purchase_location(self):
    	eq_(self.owned_book.original_purchase_location,'')

    def test_condition(self):
    	eq_(self.owned_book.condition,'unspecified')

    def test_link(self):
    	eq_(self.owned_book.link,'https://www.goodreads.com/owned_books/43018920')