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
        books = self.client.search_books("The selfish gene")
        assert len(books) > 0
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
        event = events[0]
        assert len(events) > 0
        eq_(event.gid['#text'],'56764')
        assert event.title.startswith('Carol Sklenicka')
        assert event.description.startswith('Carol Sklenicka')
        eq_(event.link,'https://www.goodreads.com/event/show/56764')
        eq_(event.venue,'Magers &amp; Quinn')
        eq_(event.address,'3038 Hennepin Avenue South')
        eq_(event.city,'Minneapolis')
        eq_(event.postal_code,'55408')
        eq_(event.state_code,'MN')
        eq_(event.country_code,'US')
        eq_(event.access,'public')
        eq_(event.event_type,'author_appearance')
        eq_(event.added_by, '788906')
        eq_(event.image_url,'https://images.gr-assets.com/authors/1265142841p2/320918.jpg')
        eq_(event.created_at,'2009-10-01T09:44:52+00:00')
        eq_(event.updated_at,'2011-05-26T22:40:35+00:00')
        eq_(event.reminder_at,'')
        eq_(event.rsvp_end_at,'')
        eq_(event.start_at,'2029-11-30T03:00:00+00:00')
        eq_(event.end_at,'2029-11-30T04:00:00+00:00')
        eq_(event.attending_count,0)
        eq_(event.responses_count,2)
        eq_(event.resource,('Author', '320918'))