Welcome to the BetterReads documentation!
=========================================

|Build Status| |Coverage Status| |Documentation Status| |Primary Code Style| |Secondary Code Style|

.. image:: http://s.gr-assets.com/assets/icons/goodreads_icon_50x50-823139ec9dc84278d3863007486ae0ac.png
:target: https://goodreads.com
    :width: 100px

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
   - Using `black code style <https://github.com/ambv/black>`__ across the board
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

You can also install BetterReads using pip. The current version on PyPi is 0.4.1.

::

    pip install betterreads


Getting Started
---------------

The first thing is to request an API key from Goodreads
`here <https://www.goodreads.com/api/keys>`__. Once you have it, you can
create a client instance to query Goodreads.

.. code:: python

    from goodreads import client
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

Contribution
------------

If you find an API method that is not supported by this package, feel
free to create a Github issue. Also, you are more than welcome to submit
a pull request for a bug fix or additional feature. For more detail on
contributing to this project and setting up your local dev environment,
check out `our contribution guide <contributing.html>`__.

License
-------

`MIT License <http://opensource.org/licenses/mit-license.php>`__

Acknowledgment
--------------

Thanks to `Paul Shannon <https://github.com/paulshannon>`__ and `Sefa Kilic <https://github.com/sefakilic>`__
for providing 'goodreads' package at PyPI, and to `Tatiana <https://github.com/tatianass>`__ and
`Rehan Khwaja <https://github.com/rkhwaja>`__ for continuing the project as goodreads2. BetterReads couldn't exist
without all of you.

.. |Build Status| image:: https://travis-ci.org/thejessleigh/betterreads.svg?branch=master
:target: https://travis-ci.org/thejessleigh/betterreads
:alt: Build Status
.. |Coverage Status| image:: https://coveralls.io/repos/github/thejessleigh/betterreads/badge.svg?branch=master
:target: https://coveralls.io/github/thejessleigh/betterreads?branch=master
:alt: Coverage Status
.. |Documentation Status| image:: https://readthedocs.org/projects/betterreads/badge/?version=latest
:target: http://betterreads.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status
.. |Primary Code Style| image:: https://camo.githubusercontent.com/28a51fe3a2c05048d8ca8ecd039d6b1619037326/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667
:target: https://github.com/ambv/black
:alt: Primary Code Style - Black
.. |Secondary Code Style| image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg
:target: https://github.com/prettier/prettier
:alt: Secondary Code Style - Prettier

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
   user_shelf
   user
   contributing

* :ref:`search`
