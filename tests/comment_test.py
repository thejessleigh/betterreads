import json
from unittest import mock

import pytest

from betterreads.client import GoodreadsClient
from betterreads.comment import GoodreadsComment


class TestComment:
    @pytest.fixture
    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_comment_list(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")
        with open("tests/fixtures/comment.json") as f:
            comment_response = f.read()
            mock_request.return_value = json.loads(comment_response)
        return client.list_comments("user", 1)

    def test_list_comments(self, test_comment_list):
        assert all(isinstance(c, GoodreadsComment) for c in test_comment_list)

    def test_gid(self, test_comment_list):
        assert test_comment_list[0].gid == "49170541"

    def test_body(self, test_comment_list):
        assert test_comment_list[0].body.startswith("I think Goodreads")

    def test_user(self, test_comment_list):
        assert test_comment_list[0].user.gid == "1246928"

    def test_created_at(self, test_comment_list):
        assert test_comment_list[0].created_at == "Thu Apr 19 20:29:12 -0700 2012"

    def test_updated_at(self, test_comment_list):
        assert test_comment_list[0].updated_at == "Thu Apr 19 20:29:12 -0700 2012"
