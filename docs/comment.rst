Comment
=======

GoodreadsComment
~~~~~~~~~~~~~~~~

GoodreadsComment is a BetterReads object for interfacing with comment data from Goodreads.

Properties
~~~~~~~~~~

- gid: Goodreads id of the comment
- body: Text body of the comment
- user: `GoodreadsUser <user.html>`__ that authored the comment
- created_at: String representation of the date when the comment was created
- updated_at: String representation of the date when the comment was updated

Usage
~~~~~

You can query Comments on a resource from the `GoodreadsClient <client.html>`__ by searching by id.

.. code:: python

    >>> from betterreads.client import GoodreadsClient

    >>> gc = GoodreadsClient('GOODREADS_API_KEY', 'GOODREADS_SECRET')
    >>> comments = gc.list_comments("review", 123456)
    >>> comment = comments[0]
    >>> comment.body
    u'This was a really good review'

When querying for a comment, you must specify which type of resource you're grabbing comments for. Valid
resource types are:

- ``author_blog_post``
- ``blog``
- ``book_news_post``
- ``chapter``
- ``comment``
- ``community_answer``
- ``event_response``
- ``fanship``
- ``friend``
- ``giveaway``
- ``giveaway_request``
- ``group_user``
- ``interview``
- ``librarian_note``
- ``link_collection``
- ``list``
- ``owned_book``
- ``photo``
- ``poll``
- ``poll_vote``
- ``queued_item``
- ``question``
- ``question_user_stat``
- ``quiz``
- ``quiz_score``
- ``rating``
- ``read_status``
- ``recommendation``
- ``recommendation_request``
- ``review``
- ``topic``
- ``user``
- ``user_challenge``
- ``user_following``
- ``user_list_challenge``
- ``user_list_vote``
- ``user_quote``
- ``user_status``
- ``video``
