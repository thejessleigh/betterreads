import collections

from betterreads.group import GoodreadsGroup
from betterreads.owned_book import GoodreadsOwnedBook
from betterreads.review import GoodreadsReview
from betterreads.user_shelf import GoodreadsUserShelf


class GoodreadsUser:
    def __init__(self, user_dict, client):
        self._user_dict = user_dict
        self._client = client  # for later queries

    def __repr__(self):
        if self.user_name:
            return self.user_name
        else:
            return self.gid

    @property
    def gid(self):
        """Goodreads ID for the user"""
        return self._user_dict["id"]

    @property
    def user_name(self):
        """Goodreads handle of the user"""
        return self._user_dict["user_name"]

    @property
    def name(self):
        """Name of the user"""
        return self._user_dict["name"]

    @property
    def link(self):
        """URL for user profile"""
        return self._user_dict["link"]

    @property
    def image_url(self):
        """URL of user image"""
        return self._user_dict["image_url"]

    @property
    def small_image_url(self):
        """URL of user image (small)"""
        return self._user_dict["small_image_url"]

    def list_groups(self, page=1):
        """List groups for the user. If there are more than 30 groups, get them
        page by page."""
        try:
            resp = self._client.request("group/list/%s.xml" % self.gid, {"page": page})
            groups = [
                GoodreadsGroup(group_dict)
                for group_dict in resp["groups"]["list"]["group"]
            ]
        except KeyError:
            groups = []
        return groups

    def owned_books(self, page=1):
        """Return the list of books owned by the user"""
        try:
            resp = self._client.session.get(
                "owned_books/user", {"page": page, "format": "xml", "id": self.gid}
            )
            owned_books_resp = resp["owned_books"]["owned_book"]
            # If there's only one owned book returned, put it in a list.
            if type(owned_books_resp) == collections.OrderedDict:
                owned_books_resp = [owned_books_resp]
            owned_books = [GoodreadsOwnedBook(d) for d in owned_books_resp]
        except KeyError:
            owned_books = []
        return owned_books

    def reviews(self, page=1):
        """Get all books and reviews on user's shelves"""
        resp = self._client.request(
            "/review/list.xml", {"v": 2, "id": self.gid, "page": page}
        )
        return [GoodreadsReview(r) for r in resp["reviews"]["review"]]

    def shelves(self, page=1):
        """Get the user's shelves. This method gets shelves only for users with
        public profile"""
        resp = self._client.request(
            "shelf/list.xml", {"user_id": self.gid, "page": page}
        )
        return [GoodreadsUserShelf(s) for s in resp["shelves"]["user_shelf"]]

    def per_shelf_reviews(self, page=1, per_page=200, shelf_name="read"):
        """Get all books and reviews on a user's particular shelf"""
        total = 1
        all_reviews = []
        while len(all_reviews) < total:
            resp = self._client.request(
                "/review/list.xml",
                {
                    "v": 2,
                    "id": self.gid,
                    "page": page,
                    "shelf": shelf_name,
                    "per_page": per_page,
                },
            )
            reviews = [GoodreadsReview(r) for r in resp["reviews"]["review"]]
            all_reviews.extend(reviews)
            page += 1
            total = int(resp["reviews"]["@total"])
        return all_reviews
