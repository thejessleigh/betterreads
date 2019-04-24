Shelf
=====

GoodreadsUserShelf
~~~~~~~~~~~~~~~~~~

``GoodreadsUserShelf`` is a class interface for the Goodreads concept of shelf. Shelves are collections of books that belong to users.

Properties
~~~~~~~~~~
- gid: Goodreads id of the shelf
- name: Name of the shelf
- exclusive: boolean flag indicating whether this shelf is mutually exclusive with other exclusive shelves
- count: number of books on a shelf
- sticky: boolean flag indicating whether this shelf is "sticky" to the top of the list in the Goodreads UI
- description: text description of the shelf
- featured: boolean flag indicating whether this is a `GoodreadsUser <user.html>`__'s featured shelf.

Usage
~~~~~

There is no method available for querying a shelf individually. Shelf data is obtained when querying for a
`GoodreadsUser <user.html>`__
