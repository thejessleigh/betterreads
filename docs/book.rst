Book
====

GoodreadsBook
-------------

A GoodreadsBook object represents the Goodreads concept of a book. It combines two concepts important to the Goodreads
API. First, is the book itself. Books have page numbers, one specific edition, one specific publisher, etc.

Books belong to a "Work" that contains aggregate information for all editions of the book.
Works have attributes like average rating, or editions.

Properties
~~~~~~~~~~

- gid: Goodreads id of the book (type: int)
- title: Title of the book (type: string)
- authors: List of `GoodreadsAuthor <author.html>`__ objects for authors credited to the work (type: list)
- description: Description of the book (type: string)
- average_rating: Mean average star rating given to the work by Goodreads users. This is a float value between 1 and 5. (type: float)
- rating_dist: Ratings distribution for the work (type: string)
- ratings_count: Number of ratings given to the work (type: int)
- text_reviews_count: Number of text reviews left for the work (type: int)
- num_pages: Number of pages in the book (type: int)
- popular_shelves: Dict of shelf names and counts that represent the number of times this work appears on a shelf named `name` on Goodreads (type: dict)
- work: Information on the book's "original work" (type: dict)
- series_works: Returns information about related works in the same series (type: dict)
- publication_date: Publication date for the book (not necessarily the original publication date) (type: datetime)
- publisher: Published listed for the book (not necessarily the original publisher) (type: string)
- language_code: Language code for the book (not necessarily the original language) (type: string)
- edition_information: Information about this specific edition of the work (type: string)
- image_url: Url to the book's cover image (type: string)
- small_image_url: Url to a smaller version of the book's cover image (type: string)
- is_ebook: ``True`` or ``False`` value for whether this book is an ebook (type: boolean)
- format: format of the book (type: string)
    - Example: "HARDCOVER"
- isbn: ISBN-10 of the book (type: string)
- isbn13: ISBN-13 of the book (type: string)
- link: link to the book's goodreads page (type: string)
- reviews_widget: widget for reviews in HTML (type: string)
- similar_books: List of `GoodreadsBook <book.html>`__ objects of books similar to this one (type: list)

Usage
~~~~~

You can query Book information from the `GoodreadsClient <client.html>`__ by searching by id.

.. code:: python

    >>> from betterreads.client import GoodreadsClient

    >>> gc = GoodreadsClient('GOODREADS_API_KEY', 'GOODREADS_SECRET')
    >>> book = gc.book(1)

    >>> book.title
    u'Harry Potter and the Half-Blood Prince (Harry Potter, #6)'
    >>> authors = book.authors
    >>> authors[0].name
    u'J.K. Rowling'
    >>> book.average_rating
    4.49

