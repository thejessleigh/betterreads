from datetime import datetime


class GoodreadsAuthor:
    def __init__(self, author_dict, client):
        self._author_dict = author_dict
        self._client = client

    def __repr__(self):
        return self.name

    @property
    def gid(self):
        """Goodreads id of the author"""
        return int(self._author_dict["id"])

    @property
    def name(self):
        """Author name"""
        return self._author_dict["name"]

    @property
    def about(self):
        """About the author"""
        return self._author_dict["about"]

    @property
    def books(self):
        """Books of the author"""
        # Goodreads API returns a list if there are more than one books, otherwise,
        # just the dict.
        from .book import GoodreadsBook

        if type(self._author_dict["books"]["book"]) == list:
            return [
                GoodreadsBook(book_dict, self._client)
                for book_dict in self._author_dict["books"]["book"]
            ]
        else:
            return [GoodreadsBook(self._author_dict["books"]["book"], self._client)]

    @property
    def born_at(self):
        """Author date of birth"""
        born_date = self._author_dict["born_at"]
        return datetime.strptime(born_date, "%Y/%m/%d")

    @property
    def died_at(self):
        """Author date of death"""
        died_date = self._author_dict["died_at"]
        return datetime.strptime(died_date, "%Y/%m/%d")

    @property
    def fans_count(self):
        """Number of fans"""
        return int(self._author_dict["fans_count"]["#text"])

    @property
    def gender(self):
        """Author gender"""
        return self._author_dict["gender"]

    @property
    def hometown(self):
        """Author's hometown"""
        return self._author_dict["hometown"]

    @property
    def link(self):
        """Link for author page"""
        return self._author_dict["link"]

    @property
    def image_url(self):
        """Image URL"""
        return self._author_dict["image_url"]

    @property
    def small_image_url(self):
        """Small image URL"""
        return self._author_dict["small_image_url"]

    @property
    def influences(self):
        """Influenced by"""
        return self._author_dict["influences"]

    @property
    def user(self):
        """Goodreads user profile of the author"""
        from betterreads.user import GoodreadsUser

        goodreads_user = None
        if "user" in self._author_dict:
            goodreads_user = GoodreadsUser(
                self._author_dict["user"]["id"]["#text"], self._client
            )
        return goodreads_user

    @property
    def works_count(self):
        """Author number of works"""
        return int(self._author_dict["works_count"])
