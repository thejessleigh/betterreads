"""
The API TOS limits to a request rate of 1 request per second per application. This decorator
can enforce that limit for single-threaded applications by setting the environmental
variable `GOODREADS_REQUEST_WAIT_MIN=1`. When not set, this decorator does nothing.
"""
import functools
import os
import time

GOODREADS_REQUEST_WAIT_MIN = float(os.environ.get("GOODREADS_REQUEST_WAIT_MIN", 0.0))


class ThrottleDecorator:

    TIME_DELTA = 0.001

    def __init__(self, request_wait_min=GOODREADS_REQUEST_WAIT_MIN):
        self.request_wait_min = request_wait_min
        # Initialize last_call so that the first call will always go through quickly.
        self.last_call = time.time() - self.request_wait_min

    def __call__(self, fn):
        @functools.wraps(fn)
        def throttled(*args, **kwargs):
            if self.request_wait_min > 0:
                # Wait until a call is allowed.
                self._wait_until_okay_to_call()
                resp = fn(*args, **kwargs)
                self.last_call = time.time()
                return resp
            else:
                return fn(*args, **kwargs)

        return throttled

    def _wait_until_okay_to_call(self):
        while time.time() - self.last_call < self.request_wait_min:
            time.sleep(self.TIME_DELTA)


throttle = ThrottleDecorator()
