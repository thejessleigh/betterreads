Author
======

GoodreadsAuthor
---------------

GoodreadsAuthor is a BetterReads object for interfacing with author data from Goodreads.

Properties
~~~~~~~~~~

- gid: Goodreads id of the author
- name: Author's name
- about: Goodreads "about the author" blurb
- books: A list of `GoodreadsBook <book.html>`__ objects for each of the author's credited works
- born_at: Author's date of birth
- died_at: Author's date of death
- fans_count: Author's number of fans on Goodreads
- gender: Author's gender
- hometown: Author's hometown
- link: Link to the author's Goodreads author page
- image_url: Url for an author's featured image on their Goodreads page
- small_image_url: Url for the small version of an author's featured image on their Goodreads page
- influences: A list of other creators the author is influenced by
- user: A `GoodreadsUser <user.html>`__ object for the author's Goodreads user profile
- works_count: A count of the works an author is credited on

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
    u'13'
    >>> author.books
    [Extremely Loud and Incredibly Close, Everything Is Illuminated, ...]
