Contribution Guide
==================

Submitting an Issue
-------------------

If you notice something is broken, a feature is missing, or you have a request to make the project better, please
feel free to submit an issue via the issue tracker. You do not need to have a solution or commit to fixing the problem
in order to create an issue. However, if you would like to contribute to the project, we would love to have your
contribution!

Fork the Repo and Create a Branch
---------------------------------

To contribute to this project, first make a fork of the repo.

Then create a branch on your local fork. This branch should be based off of the ``develop`` branch, NOT the ``master``
branch. Active development is merged into the ``develop`` branch and ``develop`` is merged into ``master`` when
there is a new release or a hotfix to be released on PyPi.

If your change corresponds to an issue your branch name should start with to that issue number.
Your name branch should be descriptive.

Example: ``13-add-delete-to-owned-book``

Once you've made your changes and the unit test suite is passing, create a pull request. Make sure that your pull
request is pointing to ``develop`` and not ``master``.


Pre-Commit
----------

This project uses pre-commit hooks to ensure consistent code style throughout the repo. We use
`black <https://github.com/ambv/black>`__ for Python files and Python code within documentation. We use
`prettier <https://github.com/prettier/prettier>`__ for all other filetypes.

Make sure you've installed all the packages listed in both ``requirements.txt`` and ``requirements-dev.txt``.
This will install pre-commit for you. Then run ``pre-commit install`` to set up the local pre-commit environment.

Pre-commit will run each time you attempt to commit staged changes. You can run the pre-commit checks at any time
using ``pre-commit run``.

Running Tests
-------------

You will not need your own developer keys to run the unit tests. However, you will need developer keys for the
Goodreads API in order to run the integration test suite.

Any changes you make likely shouldn't impact the integration tests, but if for  some reason you do need to adjust them
and run them, set your developer keys as ``GOODREADS_KEY`` and ``GOODREADS_SECRET`` environment variables.

You can obtain a Goodreads developer key `here <https://www.goodreads.com/api/keys>`__.

To run the test suite, make sure you've installed the packages listed in ``requirements.txt`` and
``requirements-dev.txt``. Then run ``pytest --cov=betterreads``

Pull requests that cause the repository's overall test coverage to drop below 85% or cause a decrease in coverage of %5
or more will be rejected. Please make sure to update tests in accordance with your changes.

Community Standards
-------------------

In general, PRs will be acknowledged within one week of receipt. I wish I could say that they would all be
reviewed and merge in in this time frame, but sometimes life gets the better of us. I'll do my best.

All contributions and discussions in this repo should abide by the `Code of Conduct <CODE_OF_CONDUCT.md>`__.
