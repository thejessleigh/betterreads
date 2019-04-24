Event
=====

GoodreadsEvent
~~~~~~~~~~~~~~
GoodreadsEvent is a BetterReads object for interfacing with event data from Goodreads.

Properties
~~~~~~~~~~

- gid: Goodreads id for the event
- title: Event's title
- description: event's description
- link: Link to the event on Goodreads
- venue: Venue information for the event
- address: Street address of the event
- city: City where the event takes place
- postal_code: Postal code for the event
- state_code: The state code of the event
- country_code: The country code for the event
- access: indicates whether the event is public or private
- event_type: indicates the type of event (ex: author reading)
- added_by: who added the event
- image_url: link to the event image
- created_at: String representation of the event's created time
- updated_at: String representation of the event's updated time
- reminder_at: String representation of the time that attendees will be reminded about the event
- rsvp_end_at: String representation of the time that RSVPs will close
- start_at: String representation of the time the event begins
- end_at: String representation of the time the event ends
- attending_count: Number of users who have RSVPd (string)
- responses_count: Number of responses (string)
- resource: Resource that the event is supporting (ex: author or book that the event is promoting)

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
