#!/usr/bin/python
import datetime

# Define event class
class dogEvent(object):
    def __init__(self, time, visitor, urinated, defocated, ate, bit, played):
        self.time = time
        self.visitor = visitor
        self.urinated = urinated
        self.defocated = defocated
        self.ate = ate
        self.bit = bit
        self.played = played

# The primary logging function
def logEvent():
    # Instantiate new sample event
    newEvent = dogEvent(datetime.datetime.now(), "James", 1, 1, 1, 0, 1)

    # Pretty-print date and time
    datestring = newEvent.time.strftime("%A, %B %d, %Y")
    timestring = newEvent.time.strftime("%I:%M %p")

    # Begin output
    print newEvent.visitor + " visited the puppy on " + datestring + " at " + timestring

# TODO: Wite a dictionary to say what the puppy did.

# TODO: Learn Flask-SQLAlchemy. http://flask-sqlalchemy.pocoo.org/2.1/quickstart/
# Some sample functions:
#   model.DogEvent.query.all() <- all events
#   model.DogEvent.query.filter_by(visitor='james').all() <- all my visits
#   model.DogEvent.query.filter_by(ate=1).all() <- all visits where the dog ate

logEvent()