.. betterreads documentation master file, created by
   sphinx-quickstart on Fri Mar 29 14:13:33 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the BetterReads documentation!
=========================================

This package provides a Python interface for the `Goodreads
API <http://goodreads.com/api>`__. Using it, you can do pretty much
anything that Goodreads allows through their public API.

This package is largely Python 2 compatible, but is only officially supported for Python 3.

Why BetterReads?
----------------

BetterReads is an expansion of the goodreads2 package available on PyPi. That package is no longer maintained
and needed some updates to be usable. The name is just cheeky and cute, and not to imply that this project is
substantially better than any other project. Someday I hope it's succeeded by a Python package called BestReads.

Major updates in this new project:

- Use https for Oauth - goodreads now requires this and previous packages' Oauth requests always fail
- Add convenience method to get all of a user's reviews for a specific shelf
- Some opinionated development changes. For example
   - No longer making live API calls in unit tests
   - Using `black code style <https://github.com/ambv/black>`__ and `prettier code style <https://github.com/prettier/prettier>`__
   - More robust `documentation <https://goodreads.readthedocs.io/en/latest/>`__

Dependencies
------------

This package depends on the following packages:

-  xmltodict
-  requests
-  rauth

They can be installed using ``pip``.

::

    sudo pip install -r requirements.txt

If you want to contribute to this package, you will need to install the packages
in ``requirements-dev.txt`` as well.

Installation
------------

To install, run the following command from the top-level package
directory.

::

    sudo python setup.py install

Getting Started
---------------

The first thing is to request an API key from Goodreads
`here <https://www.goodreads.com/api/keys>`__. Once you have it, you can
create a client instance to query Goodreads.

.. code:: python

    from betterreads import client
    gc = client.GoodreadsClient(<api_key>, <api_secret>)

To access some of the methods, you need `OAuth <http://oauth.net/>`__
for authorization.

.. code:: python

    gc.authenticate(<access_token>, <access_token_secret>)

Note that ``access_token`` and ``access_token_secret`` are different
from developer key and secret. For the development step, you can call
the same function with no parameters to get authorization. It will open
a URL pointing a Goodreads page for OAuth permission. For your
application, you can direct the user to that particular URL, ask them
to authorize your app and save the returning ``access_token`` and
``access_token_secret`` in your database.

License
-------

`MIT License <http://opensource.org/licenses/mit-license.php>`__


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   author
   book
   client
   comment
   event
   group
   owned_book
   request
   review
   session
   shelf
   user
   contributing

* :ref:`search`
