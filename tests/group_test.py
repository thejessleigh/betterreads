from nose.tools import eq_, ok_

from goodreads import apikey
from goodreads.client import GoodreadsClient


class TestGroup():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.group = client.group(1)

    def test_title(self):
        eq_(self.group.title, 'Goodreads Feedback')

    def test_gid(self):
    	eq_(self.group.gid,'1')

    def test_description(self):
    	assert self.group.description.startswith('This is a place to')

    def test_category(self):
    	eq_(self.group.category,'Business')

    def test_subcategory(self):
    	eq_(self.group.subcategory,'Companies')

    def test_rules(self):
    	assert self.group.rules.startswith('Please keep')

    def test_image_url(self):
    	eq_(self.group.image_url,'https://images.gr-assets.com/groups/1182455834p2/1.jpg')

    def test_last_activity_at(self):
    	eq_(self.group.last_activity_at,'Sun Jul 02 11:15:47 -0700 2017')

    def test_access(self):
    	eq_(self.group.access,'public')

    def test_users_count(self):
        assert len(self.group.users_count) > 1

    def test_members(self):
    	assert len(self.group.members) > 1
