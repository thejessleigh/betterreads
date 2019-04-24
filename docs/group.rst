Group
=====

GoodreadsGroup
~~~~~~~~~~~~~~

GoodreadsGroup is a BetterReads object for interfacing with group data from Goodreads.

Properties
~~~~~~~~~~

- gid: Goodreads id for the Group
- title: Title of the group
- description: Short text description of the group
- category: Text category for filtering groups (ex: Organizations)
- subcategory: Text category for further filtering groups (ex: Companies)
- rules: Text description of the rules for participating in the group
- image_url: URL for the group's featured image
- last_activity_at: String representation of the time and date of the group's last activity
- access: Indicates whether a group is public or private
- users_count: Number of users in the group (string)
- members: Dict containing information about group members. Member ids can be used to query GoodreadsUsers using the `GoodreadsClient <client.html>`__

Usage
~~~~~

You can query Group information from the `GoodreadsClient <client.html>`__ by searching by id.

.. code:: python

    >>> g = gc.find_groups("Python")
    >>> g = groups[0]
    >>> g['title']
    u'The Computer Scientists'
    >>> group = gc.group(g['id'])
    >>> group.description
    u'Only for Committed Self Learners and Computer Scientists Who are Starving for
    Information, and Want to Advance their Skills Through: Reading, Practicing and
    Discussion Computer Science and Programming Books.'
