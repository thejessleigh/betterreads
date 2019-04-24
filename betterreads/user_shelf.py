class GoodreadsUserShelf:
    """
    Interface for interacting with a GoodreadsUser's shelves
    """

    def __init__(self, shelf_dict):
        self._shelf_dict = shelf_dict

    def __repr__(self):
        return self.name

    @property
    def gid(self):
        return self._shelf_dict.get("id", {}).get("#text")

    @property
    def name(self):
        return self._shelf_dict.get("name")

    @property
    def exclusive(self):
        """
        A flag which describes whether a shelf is mutually exclusive with a user's other exclusive shelves
        """
        return self._shelf_dict.get("exclusive_flag", {}).get("#text")

    @property
    def count(self):
        """
        Number of books on a GoodreadsUserShelf
        """
        return self._shelf_dict.get("book_count", {}).get("#text")

    @property
    def sticky(self):
        """
        Describes whether a user has designated a shelf as "sticky" in the Goodreads interface
        """
        return self._shelf_dict.get("sticky", {}).get("#text")

    @property
    def description(self):
        return self._shelf_dict.get("description", {}).get("#text")

    @property
    def featured(self):
        """
        A flag which describes whether a shelf is a user's featured shelf
        """
        return self._shelf_dict.get("featured", {}).get("#text")
