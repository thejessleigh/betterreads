Owned Book
==========

GoodreadsOwnedBook
~~~~~~~~~~~~~~~~~~

GoodreadsOwnedBook is the BetterReads representation of the Goodreads concept of an "owned book."

An owned book is a representation of a physical copy of a book that is owned by a person or organization.

Properties
~~~~~~~~~~

- gid: Goodreads id for the owned book
- book: `GoodreadsBook <book.html>`__ object for the book that is "owned"
- review: `GoodreadsReview <review.html>`__ associated with the book
- current_owner: User id of the book's current owner. Can be used to query `GoodreadsUser <user.html>`__ data.
- original_purchase_date: String representation of the date that the book was purchased
- original_purchase_location: String for where the owner purchased the book
- condition: Condition of the book (ex: Brand new)
- link: Link to the Owned Book record on Goodreads

Usage
~~~~~

You can query for an owned book using the `GoodreadsClient <client.html>`__. You must have an authenticated user session
in order to query for owned books.
