User
====

GoodreadsUser
~~~~~~~~~~~~~

GoodreadsUser is a BetterReads object for interfacing with user data from Goodreads.

Properties
~~~~~~~~~~

- gid: Goodreads user id (type: int)
- user_name: Goodreads handle for the user (type: string)
- name: User's name (type: string)
- link: URL for the user profile on Goodreads (type: string)
- image_url: URL for the user's profile image (type: string)
- small_image_url: URL for a smaller version of the user's profile image (type: string)

Key Functions and Usage
~~~~~~~~~~~~~~~~~~~~~~~

Get a user using the `GoodreadsClient <client.html>`__

.. code:: python

    >>> from betterreads.client import GoodreadsClient
    >>> gc = GoodreadsClient(os.environ.get("GOODREADS_KEY"), os.environ.get("GOODREADS_SECRET"))
    >>> user = gc.user(user_id=12345)
    >>> user.name
    u'Example McTesterson'
    >>> user.user_name
    u'FlyMcTesterson63'

``list_groups``
^^^^^^^^^^^^^^^

Get a list of all the `GoodreadsGroups <group.html>`__ to which a user belongs

params:

- page (int, default=1)

return: list of `GoodreadsGroup <group.html>`__ objects

``owned_books``
^^^^^^^^^^^^^^^

Get a list of `GoodreadsOwnedBook <owned_books.html>`__ belonging to a user

params:

- page (int, default=1)

return: list of `GoodreadsOwnedBook <owned_books.html>`__ objects

``reviews``
^^^^^^^^^^^

Get a list of a user's `GoodreadsReview <review.html>`__

params:

- page (int, default=1)

return: list of `GoodreadsReview <review.html>`__ objects

``shelves``
^^^^^^^^^^^

Get a list of user's `GoodreadsUserShelf <user_shelf.html>`__ objects

params:

- page (int, default=1)

return: list of `GoodreadsUserShelf <user_shelf.html>`__ objects

``per_shelf_reviews``
^^^^^^^^^^^^^^^^^^^^^

Get a list of `GoodreadsBook <book.html>`__ objects belonging to a particular `GoodreadsUserShelf <user_shelf.html>`__

params:

- page (int, default=1)
- per_page (int, default=200)
- shelf_name (string, default="read)

return: list of `GoodreadsReview <review.html>`__ objects

