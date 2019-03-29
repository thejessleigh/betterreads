from nose.tools import eq_, ok_

from betterreads.comment import GoodreadsComment
from tests.test_fixture import GoodreadsTestClass


class TestComment(GoodreadsTestClass):
    @classmethod
    def setup_class(cls):
        GoodreadsTestClass.setup_class()
        cls.comments = cls.client.list_comments("user", "1")
        cls.comment = cls.comments[0]

    def test_list_comments(self):
        ok_(all(isinstance(c, GoodreadsComment) for c in self.comments))

    def test_gid(self):
        eq_(self.comment.gid, "49170541")

    def test_body(self):
        assert self.comment.body.startswith("I think Goodreads")

    def test_user(self):
        eq_(self.comment.user.gid, "1246928")

    def test_created_at(self):
        eq_(self.comment.created_at, "Thu Apr 19 20:29:12 -0700 2012")

    def test_updated_at(self):
        eq_(self.comment.updated_at, "Thu Apr 19 20:29:12 -0700 2012")
