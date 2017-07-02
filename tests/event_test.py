from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.event import GoodreadsEvent
from nose.tools import eq_, ok_

class TestEvent():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.events = client.list_events(55408)
        cls.event = cls.events[0]

    def test_list_events(self):
    	assert all(isinstance(e, GoodreadsEvent) for e in self.events)

    def test_repr(self):	
    	eq_(self.event.resource,('Author', '320918'))

    def test_repr(self):
    	eq_(repr(self.event), self.event.title)

    def test_gid(self):
    	eq_(self.event.gid['#text'],'56764')

    def test_title(self):
    	assert self.event.title.startswith('Carol Sklenicka')

    def test_description(self):
    	assert self.event.description.startswith('Carol Sklenicka')

    def test_link(self):
    	eq_(self.event.link,'https://www.goodreads.com/event/show/56764')

    def test_venue(self):
    	eq_(self.event.venue,'Magers &amp; Quinn')

    def test_address(self):
    	eq_(self.event.address,'3038 Hennepin Avenue South')

    def test_city(self):
    	eq_(self.event.city,'Minneapolis')

    def test_postal_code(self):
    	eq_(self.event.postal_code,'55408')

    def test_state_code(self):
    	eq_(self.event.state_code,'MN')

    def test_country_code(self):
    	eq_(self.event.country_code,'US')

    def test_access(self):
    	eq_(self.event.access,'public')

    def test_event_type(self):
    	eq_(self.event.event_type,'author_appearance')

    def test_added_by(self):
    	eq_(self.event.added_by, '788906')

    def test_image_url(self):
    	eq_(self.event.image_url,'https://images.gr-assets.com/authors/1265142841p2/320918.jpg')

    def test_created_at(self):
    	eq_(self.event.created_at,'2009-10-01T09:44:52+00:00')

    def test_updated_at(self):
    	eq_(self.event.updated_at,'2011-05-26T22:40:35+00:00')

    def test_reminder_at(self):
    	eq_(self.event.reminder_at,'')

    def test_rsvp_end_at(self):
    	eq_(self.event.rsvp_end_at,'')

    def test_start_at(self):
    	eq_(self.event.start_at,'2029-11-30T03:00:00+00:00')

    def test_end_at(self):
    	eq_(self.event.end_at,'2029-11-30T04:00:00+00:00')

    def test_attending_count(self):
    	eq_(self.event.attending_count,0)

    def test_responses_count(self):
    	eq_(self.event.responses_count,2)