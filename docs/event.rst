Event
=====

GoodreadsEvent
~~~~~~~~~~~~~~
GoodreadsEvent is a BetterReads object for interfacing with event data from Goodreads.

Properties
~~~~~~~~~~

- gid: Goodreads id for the event (type: int)
- title: Event's title (type: string)
- description: event's description (type: string)
- link: Link to the event on Goodreads (type: string)
- venue: Venue information for the event (type: string)
- address: Street address of the event (type: string)
- city: City where the event takes place (type: string)
- postal_code: Postal code for the event (type: string)
- state_code: The state code of the event (type: string)
- country_code: The country code for the event (type: string)
- access: indicates whether the event is public or private (type: string)
- event_type: indicates the type of event (type: string)
    - Example: author reading
- added_by: user id for who added the event (type: int)
- image_url: link to the event image (type: string)
- created_at: String representation of the event's created time (type: datetime)
- updated_at: String representation of the event's updated time (type: datetime)
- reminder_at: String representation of the time that attendees will be reminded about the event (type: datetime)
- rsvp_end_at: String representation of the time that RSVPs will close (type: datetime)
- start_at: String representation of the time the event begins (type: datetime)
- end_at: String representation of the time the event ends (type: datetime)
- attending_count: Number of users who have RSVPd (type: int)
- responses_count: Number of responses (type: int)
- resource: Resource that the event is supporting (type: tuple)
    - Example: author or book that the event is promoting

Usage
~~~~~

You can query Events within or near a zip code with the `GoodreadsClient <client.html>`__ by searching by zip.

.. code:: python

    >>> from betterreads.client import GoodreadsClient

    >>> gc = GoodreadsClient('GOODREADS_API_KEY', 'GOODREADS_SECRET')
    >>> events = gc.list_events(80126)
    >>> events[0]
    >>> event.title
    u'Meet and Greet with Mary Sue'
    >>> event.description
    u'Learn all about Mary Sue and her epic adventures!'
