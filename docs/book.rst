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

- gid: Goodreads id of the book
- title: Title of the book
- authors: List of `GoodreadsAuthor <author.html>`__ objects for authors credited to the work
- description: Description of the book
- average_rating: Mean average star rating given to the work by Goodreads users. This is a float value between 1 and 5.
- rating_dist: Ratings distribution for the work
- ratings_count: Number of ratings given to the work
- text_reviews_count: Number of text reviews left for the work
- num_pages: Number of pages in the book
- popular_shelves: Dict of shelf names and counts that represent the number of times this work appears on a shelf named `name` on Goodreads
- work: Information on the book's "original work"
- series_works: Returns information about related works in the same series
- publication_date: Publication date for the book (not necessarily the original publication date)
- publisher: Published listed for the book (not necessarily the original publisher)
- language_code: Language code for the book (not necessarily the original language)
- edition_information: Information about this specific edition of the work
- image_url: Url to the book's cover image
- small_image_url: Url to a smaller version of the book's cover image
- is_ebook: ``true`` or ``false`` value for whether this book is an ebook
- format: format of the book
    - example: "HARDCOVER"
- isbn: ISBN-10 of the book
- isbn13: ISBN-13 of the book
- link: link to the book's goodreads page
- reviews_widget: widget for reviews in HTML
- similar_books: List of `GoodreadsBook <book.html>`__ objects of books similar to this one

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
    u'4.49'

