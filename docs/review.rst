Review
======

GoodreadsReview
~~~~~~~~~~~~~~~

Betterreads interface for interacting with Goodreads review data.

Properties
~~~~~~~~~~

- gid: Goodreads review id
- book: Dict with information on the book the review belongs to
- rating: Review rating from 1 - 5 "stars"
- shelves: Most common shelf names that contain this book
- recommended_for: dict of users recommended for
- recommended_by: dict of users recommended by
- started_at: String representation of the date the user started reading the book
- read_at: String representation of the date the user finished reading the book
- body: Text body of the review
- comments_count: Number of comments on the review (string)
- url: Link to the review on Goodreads
- owned: boolean value (expressed as "0" or "1") whether the user owns this book


Usage
~~~~~

You can query Reviews by id using the `GoodreadsClient <client.html>`__.

.. code:: python

    >>> from betterreads.client import GoodreadsClient

    >>> gc = GoodreadsClient('GOODREADS_API_KEY', 'GOODREADS_SECRET')
    >>> review = gc.review(1)
    >>> review.body
    u'I was lukewarm on this book'
    >>> review.owned
    u'0'


