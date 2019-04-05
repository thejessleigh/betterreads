from unittest import skip

from betterreads.author import GoodreadsAuthor
from betterreads.book import GoodreadsBook
from tests.test_fixture import GoodreadsTestClass


class TestAuthor(GoodreadsTestClass):
    @classmethod
    def setup_class(cls):
        GoodreadsTestClass.setup_class()
        cls.author = cls.client.author("64941")

    def test_get_author(self):
        assert isinstance(self.author, GoodreadsAuthor)
        assert self.author.gid == "64941"
        assert repr(self.author) == "Donald Ervin Knuth"

    def test_author_name(self):
        assert self.author.name == "Donald Ervin Knuth"

    def test_author_about(self):
        assert self.author.about.startswith(
            "Donald Ervin Knuth, born January 10th 1938,"
        )

    def test_author_books(self):
        books = self.author.books
        assert all(isinstance(book, GoodreadsBook) for book in books)
        assert books[-1].title == "Literate Programming"

    def test_author_with_one_book(self):
        books = self.client.author("5734084").books
        assert len(books) == 1

    def test_born_at(self):
        assert self.author.born_at == "1938/01/10"

    def test_died_at(self):
        author = self.client.author("3565")
        assert author.died_at == "1900/11/30"

    @skip(
        "Skip until test fixtures w/o live calls - live calls are subject to change & break tests"
    )
    def test_fans_count(self):
        assert self.author.fans_count() == "240"

    def test_gender(self):
        assert self.author.gender == "male"

    def test_hometown(self):
        assert self.author.hometown == "Milwaukee"

    def test_link(self):
        assert (
            self.author.link
            == "https://www.goodreads.com/author/show/64941.Donald_Ervin_Knuth"
        )

    def test_image_url(self):
        assert (
            self.author.image_url
            == "https://images.gr-assets.com/authors/1236845611p5/64941.jpg"
        )

    def test_small_image_url(self):
        assert (
            self.author.small_image_url
            == "https://images.gr-assets.com/authors/1236845611p2/64941.jpg"
        )

    def test_influences(self):
        assert self.author.influences is None

    def test_user(self):
        assert self.author.user is None

    @skip(
        "Skip until test fixtures w/o live calls - live calls are subject to change & break tests"
    )
    def test_works_count(self):
        assert self.author.works_count == "59"
