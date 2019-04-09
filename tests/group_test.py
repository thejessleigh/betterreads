import pytest


@pytest.mark.skip(reason="Test suite pending rewrite.")
class TestGroup:
    @classmethod
    def setup_class(cls):
        cls.group = cls.client.group(1)

    def test_title(self):
        eq_(self.group.title, "Goodreads Feedback")

    def test_gid(self):
        eq_(self.group.gid, "1")

    def test_description(self):
        assert self.group.description.startswith("Welcome to the Feedback Group!")

    def test_category(self):
        eq_(self.group.category, "Business")

    def test_subcategory(self):
        eq_(self.group.subcategory, "Companies")

    def test_rules(self):
        assert self.group.rules.startswith("To help")

    def test_image_url(self):
        eq_(
            self.group.image_url,
            "https://images.gr-assets.com/groups/1182455834p2/1.jpg",
        )

    def test_access(self):
        eq_(self.group.access, "public")

    def test_users_count(self):
        assert len(self.group.users_count) > 1

    def test_members(self):
        assert len(self.group.members) > 1
