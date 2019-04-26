from datetime import datetime

from betterreads.user import GoodreadsUser


class GoodreadsComment:
    """Goodreads comment class"""

    def __init__(self, comment_dict):
        self._comment_dict = comment_dict

    @property
    def gid(self):
        """Goodreads id of the comment"""
        return int(self._comment_dict["id"])

    @property
    def body(self):
        """Body of the comment"""
        return self._comment_dict["body"]

    @property
    def user(self):
        """User that made the comment"""
        return GoodreadsUser(self._comment_dict["user"], self)

    @property
    def created_at(self):
        """Comment created at"""
        return datetime.strptime(
            self._comment_dict["created_at"], "%a %b %d %H:%M:%S %z %Y"
        )

    @property
    def updated_at(self):
        """Comment updated at"""
        return datetime.strptime(
            self._comment_dict["updated_at"], "%a %b %d %H:%M:%S %z %Y"
        )
