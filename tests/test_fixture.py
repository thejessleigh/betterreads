import os

from betterreads.client import GoodreadsClient


class GoodreadsTestClass:
    @classmethod
    def setup_class(cls):
        cls.client = GoodreadsClient(
            os.environ.get("GOODREADS_KEY"), os.environ.get("GOODREADS_SECRET")
        )
        cls.client.authenticate(
            os.environ.get("GOODREADS_OAUTH_TOKEN"),
            os.environ.get("GOODREADS_OAUTH_SECRET"),
        )
