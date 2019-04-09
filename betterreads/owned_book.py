"""Class definition for owned books"""

from betterreads.book import GoodreadsBook
from betterreads.review import GoodreadsReview


class GoodreadsOwnedBook:
    def __init__(self, owned_book_dict):
        self._owned_book_dict = owned_book_dict

    @property
    def gid(self):
        """Goodreads id of the owned book"""
        return self._owned_book_dict["id"]["#text"]

    @property
    def book(self):
        """Book owned"""
        return GoodreadsBook(self._owned_book_dict["book"], self)

    @property
    def review(self):
        """Review for the owned book"""
        return GoodreadsReview(self._owned_book_dict["review"])

    @property
    def current_owner(self):
        """Return current owner's id"""
        return self._owned_book_dict["current_owner_id"]["#text"]

    @property
    def original_purchase_date(self):
        """Date of purchase"""
        date_field = self._owned_book_dict.get("original_purchase_date", None)
        if date_field:
            return date_field.get("#text", None)
        else:
            return None

    @property
    def original_purchase_location(self):
        """Purchase location"""
        return self._owned_book_dict.get("original_purchase_location", None)

    @property
    def condition(self):
        """Condition of the book"""
        return self._owned_book_dict["condition"]

    @property
    def link(self):
        """Linked for the owned book"""
        return self._owned_book_dict["link"]
