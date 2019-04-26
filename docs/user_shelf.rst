Shelf
=====

GoodreadsUserShelf
~~~~~~~~~~~~~~~~~~

``GoodreadsUserShelf`` is a class interface for the Goodreads concept of shelf. Shelves are collections of books that belong to users.

Properties
~~~~~~~~~~
- gid: Goodreads id of the shelf (type: int)
- name: Name of the shelf (type: string)
- exclusive: boolean flag indicating whether this shelf is mutually exclusive with other exclusive shelves (type: boolean)
- count: number of books on a shelf (type: integer)
- sticky: boolean flag indicating whether this shelf is "sticky" to the top of the list in the Goodreads UI (type: boolean)
- description: text description of the shelf (type: string)
- featured: boolean flag indicating whether this is a `GoodreadsUser <user.html>`__'s featured shelf. (type: boolean)

Usage
~~~~~

There is no method available for querying a shelf individually. Shelf data is obtained when querying for a
`GoodreadsUser <user.html>`__
