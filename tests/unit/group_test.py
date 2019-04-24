import json
from unittest import mock

import pytest

from betterreads.client import GoodreadsClient


class TestGroup:
    @pytest.fixture
    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_group(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")

        # Goodreads Group data pulled on 2019-04-09. Lightly modified for testing purposes
        with open("tests/unit/fixtures/group.json") as f:
            group_response = f.read()
            mock_request.return_value = json.loads(group_response)
        return client.group(8095)

    def test_title(self, test_group):
        assert test_group.title == "Goodreads Developers"

    def test_gid(self, test_group):
        assert test_group.gid == "8095"

    def test_description(self, test_group):
        assert test_group.description.startswith(
            "Official group for developers on Goodreads"
        )

    def test_category(self, test_group):
        assert test_group.category == "Organizations"

    def test_subcategory(self, test_group):
        assert test_group.subcategory == "Companies"

    def test_rules(self, test_group):
        assert test_group.rules == "This is a test string"

    def test_image_url(self, test_group):
        assert (
            test_group.image_url
            == "https://images.gr-assets.com/groups/1220414390p2/8095.jpg"
        )

    def test_access(self, test_group):
        assert test_group.access == "public"

    def test_users_count(self, test_group):
        assert test_group.users_count == "2028"

    def test_members(self, test_group):
        assert len(test_group.members) > 1

    def test_last_activity_at(self, test_group):
        assert test_group.last_activity_at == "Tue Apr 09 10:55:32 -0700 2019"
