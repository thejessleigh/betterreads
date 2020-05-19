Client
======

GoodreadsClient
---------------

The GoodreadsClient is the wrapper that powers direct queries to the Goodreads API.  It throttles requests to one per second, as required by Goodreads' terms and conditions.

Fields
~~~~~~
- client_key: Application's Goodreads API Client Key
- client_secret: Application's Goodreads API Client Secret
- diskcache: a diskcache cache instance (optional)


Properties
~~~~~~~~~~
- query_dict: A dict containing a GoodreadsClient's client_key

Key Functions and Usage
~~~~~~~~~~~~~~~~~~~~~~~

Instantiate Client
^^^^^^^^^^^^^^^^^^

.. code:: python

    >>> from betterreads.client import client
    >>> gc = client.GoodreadsClient(<api_key>, <api_secret>)

or, with cache:

.. code:: python

    >>> from diskcache import Cache
    >>> cache = Cache()
    >>> from betterreads import client
    >>> gc = client.GoodreadsClient(<api_key>, <api_secret>, cache)

``author``
^^^^^^^^^^

Get information about an author, querying by Goodreads author id.

params:

- author_id (int)

return: `GoodreadsAuthor <author.html>`__ object

.. code:: python

    >>> author = gc.author(2618)
    >>> author.name
    u'Jonathan Safran Foer'

``find_author``
^^^^^^^^^^^^^^^

Get information about an author querying by name.

params:

- author_name (string)

return: `GoodreadsAuthor <author.html>`__ object or ``None``

    >>> author = gc.find_author("Stephen King")
    >>> author.gid
    '3389'

``book``
^^^^^^^^

Get information about a book querying by Goodreads book id or ISBN.

params:

- book_id (int) (optional)
- book_isbn (int or string) (optional)

return: `GoodreadsBook <book.html>`__ object

.. code:: python

    >>> book = gc.book(123)
    >>> book.title
    u'The Power of One (The Power of One, #1)'
    >>> book.num_pages
    '291'

``search_books``
^^^^^^^^^^^^^^^^

Get the most popular books for a given query. Searches title, author, and genre.

params:

- q (string)
- page (int, deftault=1)
- search_field (string, default="all")
    - valid options: ['title', 'author', 'genre', 'all']

return: List of `GoodreadsBook <book.html>`__ objects.

return: list of matching `GoodreadsBook <book.html>`__ objects

.. code:: python

    >>> books = gc.search_books("Shakespeare King")
    >>> print(books)
    [King Lear,
     Hamlet,
     Manga Shakespeare: King Lear,
     Macbeth,
     A Midsummer Night's Dream,
     Julius Caesar,
     The Merchant of Venice,
     Twelfth Night,
     King Henry IV, Part 1,
     Shakespeare's King Lear (Cliffs Notes),
     The Complete Works of Shakespeare,
     Richard III,
     Henry V,
     Prefaces to Shakespeare: King Lear,
     Four Great Tragedies: Hamlet / Othello / King Lear / Macbeth,
     The Winter's Tale,
     The Comedy of Errors,
     William Shakespeare, "King Lear",
     King Richard II (The Arden Shakespeare),
     Shakespeare's Ovid: Being Arthur Golding's Translation Of The Metamorphoses]


``search_books_total_pages``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get the total number of pages for a book search. Accepts text for the query param and searches title, author, and genre.

params:

- q (string)
- page (int, default=1)
- search_field (string, default='all')
    - valid options: ['title', 'author', 'genre', 'all']

return: integer number of results pages for the query string

.. code:: python

    >>> gc.search_books_total_pages("Shakespeare King")
    41

``search_books_all_pages``
^^^^^^^^^^^^^^^^^^^^^^^^^^

Get all the books for a given query. This will return all books where the title/author/genre fields show matches.
Sorted by popularity on Goodreads. Note that if you use a broad search term this operation could take a while.

params:

- q (string)
- page (int, default=1)
- search_field (string, default='all')
    - valid options ['title', 'author', 'genre', 'all']

return: List of `GoodreadsBook <book.html>`__ objects

.. code:: python

    >>> books = gc.search_books_all_pages("Demon in my View", search_field="title")
    >>> print(books)
    [Demon in My View,
     A Demon in My View,
     Demon in My View,
     Of a Demon in My View,
     Of a Demon in My View,
     A Demon in My View,
     The Tree of Hands / A Demon in My View,
     A Demon In My View,
     The face of trespass: A judgement in stone ; A demon in my view,
     A Demon in My View (Prose series) (Prose series),
     A Demon in My View (Prose Series 68),
     Novels by Amelia Atwater-Rhodes: Falcondance, Demon in My View, Hawksong, Wyvernhail, Snakecharm, Shattered Mirror, Midnight Predator,
     Nyeusigrube: The Kiesha'ra Series, Amelia Atwater-Rhodes, Demon in My View, Shattered Mirror, in the Forests of the Night,
     Articles on Nyeusigrube, Including: In the Forests of the Night, Demon in My View, Shattered Mirror, Midnight Predator, Hawksong, Snakecharm, Falcondance, Wyvernhail, Zane Cobriana, Amelia Atwater-Rhodes, the Kiesha'ra Series,
     The Ruth Rendell Omnibus: "Face of Trespass", "Judgement in Stone", "Demon in My View" v. 1]

``group``
^^^^^^^^^

Get information about a group. Queries the Goodreads API by group id.

params:

- group_id (int or string)

return: `GoodreadsGroup <group.html>`__

.. code:: python

    >>> gc.group(8095)
    u'Goodreads Developers'

``owned_book``
^^^^^^^^^^^^^^

Get info about an owned book. Queries the Goodreads API by id. This method requires user authentication.

params:

- owned_book_id (int or string)

return: `GoodreadsOwnedBook <owned_book.html>`__ object


``find_groups``
^^^^^^^^^^^^^^^

Find groups based based on a text query.

params:

    - query (string)
    - page (int, default=1)

return: List of OrderedDicts


``request``
^^^^^^^^^^^

create a `GoodreadsRequest <request.html>`__ object and make a request to the Goodreads API.



``user``
^^^^^^^^

Get information on a goodreads user, querying either by Goodreads id or username. Returns a `GoodreadsUser <user.html>`__ object.

.. code:: python

    >>> user = gc.user(user_id=12345)
    >>> user.name
    u'Example McTesterson'

    >>> user = gc.user(username="test_username")
    >>> user.name
    u'Test Name Person III'





GoodreadsClientException
------------------------

An ``Exception`` that is raised when the ``GoodreadsClient`` encounters an error executing a request

