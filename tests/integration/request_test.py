import os

import pytest

from betterreads.client import GoodreadsClient
from betterreads.request import GoodreadsRequest, GoodreadsRequestException


class TestRequest:
    def test_valid_request(self):
        client = GoodreadsClient(
            os.environ.get("GOODREADS_KEY"), os.environ.get("GOODREADS_SECRET")
        )
        args = ["book/show", {"id": 1, "key": os.environ.get("GOODREADS_KEY")}]
        kwargs = {}
        request = GoodreadsRequest(client, *args, **kwargs)
        assert isinstance(request, GoodreadsRequest)

        resp = request.request()
        assert isinstance(resp, dict)

    def test_invalid_request(self):
        client = GoodreadsClient(
            os.environ.get("GOODREADS_KEY"), os.environ.get("GOODREADS_SECRET")
        )
        args = ["book/show", {"id": "ibx", "key": os.environ.get("GOODREADS_KEY")}]
        kwargs = {}
        request = GoodreadsRequest(client, *args, **kwargs)

        with pytest.raises(GoodreadsRequestException):
            request.request()
