Group
=====

GoodreadsGroup
~~~~~~~~~~~~~~

GoodreadsGroup is a BetterReads object for interfacing with group data from Goodreads.

Properties
~~~~~~~~~~

- gid: Goodreads id for the Group (type: int)
- title: Title of the group (type: string)
- description: Short text description of the group (type: string)
- category: Text category for filtering groups (type: string)
    - Example: Organizations
- subcategory: Text category for further filtering groups (type: string)
    - Example: Companies
- rules: Text description of the rules for participating in the group (type: string)
- image_url: URL for the group's featured image (type: string)
- last_activity_at: String representation of the time and date of the group's last activity (type: datetime)
- access: Indicates whether a group is public or private (type: string)
- users_count: Number of users in the group (type: int)
- members: List of dicts containing information about group members. Member ids can be used to query GoodreadsUsers using the `GoodreadsClient <client.html>`__ (type: list)

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
