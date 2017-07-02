from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.author import GoodreadsAuthor
from goodreads.book import GoodreadsBook


class TestAuthor():
    @classmethod
    def setup_class(cls):
        cls.client = GoodreadsClient(apikey.key, apikey.secret)
        cls.client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.author = cls.client.author('64941')

    def test_get_author(self):
        assert isinstance(self.author, GoodreadsAuthor)
        assert self.author.gid == '64941'
        assert repr(self.author) == 'Donald Ervin Knuth'

    def test_author_name(self):
        assert self.author.name == 'Donald Ervin Knuth'

    def test_author_about(self):
        assert self.author.about.startswith('Donald Ervin Knuth, born January 10th 1938,')

    def test_author_books(self):
        books = self.author.books
        assert all(isinstance(book, GoodreadsBook) for book in books)
        assert (books[-1].title == 'Literate Programming')

    def test_author_with_one_book(self):
        books = self.client.author('5734084').books
        assert len(books) == 1

    def test_born_at(self):
        assert self.author.born_at == '1938/01/10'

    def test_died_at(self):
        author = self.client.author('3565')
        assert author.died_at == '1900/11/30'

    def test_fans_count(self):
        assert self.author.fans_count()['#text'] == '240'

    def test_gender(self):
        assert self.author.gender == 'male'

    def test_hometown(self):
        assert self.author.hometown == 'Milwaukee'

    def test_link(self):
        assert self.author.link == 'https://www.goodreads.com/author/show/64941.Donald_Ervin_Knuth'

    def test_image_url(self):
        assert self.author.image_url == 'https://images.gr-assets.com/authors/1236845611p5/64941.jpg'

    def test_small_image_url(self):
        assert self.author.small_image_url == 'https://images.gr-assets.com/authors/1236845611p2/64941.jpg'

    def test_influences(self):
        assert self.author.influences is None

    def test_user(self):
        assert self.author.user is None

    def test_works_count(self):
        assert self.author.works_count == '59'
