#!/usr/bin/python
import datetime

# Define event class
class Event(object):
    def __init__(self):
        self.time = datetime.datetime.utcnow()

# Instantiate new event
newEvent = Event()
print newEvent.time