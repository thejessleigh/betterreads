from datetime import datetime
import json
from unittest import mock

import pytest

from betterreads.client import GoodreadsClient
from betterreads.event import GoodreadsEvent


class TestEvent:
    @pytest.fixture
    @mock.patch("betterreads.client.GoodreadsClient.request")
    def test_event_list(self, mock_request):
        client = GoodreadsClient("GOODREADS_KEY", "GOODREADS_SECRET")
        with open("tests/unit/fixtures/event.json") as f:
            event_response = f.read()
            mock_request.return_value = json.loads(event_response)
        return client.list_events(80126)

    @pytest.fixture
    def test_event(self, test_event_list):
        return test_event_list[0]

    def test_list_events(self, test_event_list):
        assert all(isinstance(e, GoodreadsEvent) for e in test_event_list)

    def test_resource(self, test_event):
        assert test_event.resource == ("Author", 21246)

    def test_repr(self, test_event):
        assert repr(test_event) == test_event.title

    def test_gid(self, test_event):
        assert test_event.gid == 1048832

    def test_title(self, test_event):
        assert test_event.title == "Outer Order Inner Calm Book Tour: Highland Park, CO"

    def test_description(self, test_event):
        assert test_event.description.startswith(
            "Douglas County Library and Tattered Cover Book Store present a talk"
        )

    def test_link(self, test_event):
        assert test_event.link == "https://www.goodreads.com/event/show/1048832"

    def test_venue(self, test_event):
        assert test_event.venue == "Denver Marriott"

    def test_address(self, test_event):
        assert test_event.address == "10345 Pak Meadows Dr,"

    def test_city(self, test_event):
        assert test_event.city == "Lone Tree"

    def test_postal_code(self, test_event):
        assert test_event.postal_code == "80124"

    def test_state_code(self, test_event):
        assert test_event.state_code == "CO"

    def test_country_code(self, test_event):
        assert test_event.country_code == "US"

    def test_access(self, test_event):
        assert test_event.access == "public"

    def test_event_type(self, test_event):
        assert test_event.event_type == "author_appearance"

    def test_added_by(self, test_event):
        assert test_event.added_by == 2547702

    def test_image_url(self, test_event):
        assert (
            test_event.image_url
            == "https://images.gr-assets.com/authors/1252934548p2/21246.jpg"
        )

    def test_created_at(self, test_event):
        assert isinstance(test_event.created_at, datetime)

    def test_updated_at(self, test_event):
        assert isinstance(test_event.updated_at, datetime)

    def test_reminder_at(self, test_event):
        assert isinstance(test_event.reminder_at, datetime)

    def test_none_reminder_at(self, test_event_list):
        event = test_event_list[1]
        assert event.reminder_at is None

    def test_rsvp_end_at(self, test_event):
        assert isinstance(test_event.rsvp_end_at, datetime)

    def test_none_rsvp_end_at(self, test_event_list):
        event = test_event_list[1]
        assert event.rsvp_end_at is None

    def test_start_at(self, test_event):
        assert isinstance(test_event.start_at, datetime)

    def test_end_at(self, test_event):
        assert isinstance(test_event.end_at, datetime)

    def test_attending_count(self, test_event):
        assert test_event.attending_count == 0

    def test_responses_count(self, test_event):
        assert test_event.responses_count == 0
