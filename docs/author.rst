Author
======

GoodreadsAuthor
---------------

GoodreadsAuthor is a BetterReads object for interfacing with author data from Goodreads.

Properties
~~~~~~~~~~

- gid: Goodreads id of the author (type: int)
- name: Author's name (type: string)
- about: Goodreads "about the author" blurb (type: string)
- books: A list of `GoodreadsBook <book.html>`__ objects for each of the author's credited works (type: list)
- born_at: Author's date of birth (type: datetime)
- died_at: Author's date of death (type: datetime)
- fans_count: Author's number of fans on Goodreads (type: int)
- gender: Author's gender (type: string)
- hometown: Author's hometown (type: string)
- link: Link to the author's Goodreads author page (type: string)
- image_url: Url for an author's featured image on their Goodreads page (type: string)
- small_image_url: Url for the small version of an author's featured image on their Goodreads page (type: string)
- influences: A list of other creators the author is influenced by (type: string)
- user: A `GoodreadsUser <user.html>`__ object for the author's Goodreads user profile (type: `GoodreadsUser <user.html>`__)
- works_count: A count of the works an author is credited on (type: int)

Usage
~~~~~

You can query Author information from the `GoodreadsClient <client.html>`__ by searching by id.

.. code:: python

    >>> from betterreads.client import GoodreadsClient

    >>> gc = GoodreadsClient('GOODREADS_API_KEY', 'GOODREADS_SECRET')
    >>> author = gc.author(2617)
    >>> author.name
    u'Jonathan Safran Foer'
    >>> author.works_count
    13
    >>> author.books
    [Extremely Loud and Incredibly Close, Everything Is Illuminated, ...]
