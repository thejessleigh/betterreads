Review
======

GoodreadsReview
~~~~~~~~~~~~~~~

Betterreads interface for interacting with Goodreads review data.

Properties
~~~~~~~~~~

- gid: Goodreads review id (type: int)
- book: Dict with information on the book the review belongs to (type: dict)
- rating: Review rating from 1 - 5 "stars" (type: int)
- shelves: Most common shelf names that contain this book (type: list)
- recommended_for: dict of users recommended for (type: dict)
- recommended_by: dict of users recommended by (type: dict)
- started_at: String representation of the date the user started reading the book (type: datetime)
- read_at: String representation of the date the user finished reading the book (type: datetime)
- body: Text body of the review (type: string)
- comments_count: Number of comments on the review (type: int)
- url: Link to the review on Goodreads (type: string)
- owned: boolean value (expressed as "0" or "1") whether the user owns this book (type: boolean)


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
    False


