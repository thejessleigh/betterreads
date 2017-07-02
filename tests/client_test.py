"""Client test functions"""

from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.book import GoodreadsBook
from nose.tools import eq_, ok_

class TestClient():
    @classmethod
    def setup_class(cls):
        cls.client = GoodreadsClient(apikey.key, apikey.secret)
        cls.client.authenticate(apikey.oauth_access_token,
                                apikey.oauth_access_token_secret)

    def test_client_setup(self):
        eq_(self.client.client_key,apikey.key)
        eq_(self.client.client_secret,apikey.secret)

    def test_auth_user(self):
        user = self.client.auth_user()
        assert user.user_name is None

    def test_user_info(self):
        user = self.client.user(1)
        eq_(user.user_name,'otis')

    def test_author_by_id(self):
        author_id = '8566992'
        author = self.client.author(author_id)
        eq_(author.gid,author_id)

    def test_author_by_name(self):
        author_name = 'Richard Dawkins'
        author = self.client.find_author(author_name)
        eq_(author.name,author_name)

    def test_book_by_id(self):
        book_id = '11870085'
        book = self.client.book(book_id)
        eq_(book.gid,book_id)

    def test_search_books(self):
        books = self.client.search_books(q='Gerri Hill', search_field='author')
        assert len(books) == 20
        assert all(isinstance(book, GoodreadsBook) for book in books)

    def test_search_books_with_one_book(self):
        books = self.client.search_books("Childhood, Boyhood, Truth: From an African Youth to the Selfish Gene")
        eq_(len(books),1)
        assert all(isinstance(book, GoodreadsBook) for book in books)

    def test_group_by_id(self):
        group_id = '1'
        group = self.client.group(group_id)
        eq_(group.gid,group_id)

    def test_find_groups(self):
        groups = self.client.find_groups('Goodreads Developers')
        assert len(groups) > 1

    def test_list_events(self):
        events = self.client.list_events(55408)
        assert len(events) > 0

    def test_search_books_total_pages(self):
        num_pages = self.client.search_books_total_pages(q='Gerri Hill', search_field='author')
        eq_(num_pages, 2)

    def test_search_books_all_pages(self):
        books = self.client.search_books_all_pages(q='Gerri Hill', search_field='author')
        assert len(books) > 20
