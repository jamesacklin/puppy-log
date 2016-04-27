#!/usr/bin/python
import datetime

# Define event class
class dogEvent(object):
    def __init__(self, time, visitor, behaviors):
        self.time = time
        self.visitor = visitor
        self.behaviors = behaviors

# Instantiate new sample event
newEvent = dogEvent(datetime.datetime.now(), "James", ["peed", "pooped", "ate", "bit me", "played"])

# Begin output
print "%s visited the puppy on %s at %s" % (newEvent.visitor, newEvent.time.strftime("%A, %B %d, %Y"), newEvent.time.strftime("%I:%M %p"))
print "The puppy " + ', '.join([str(behavior) for behavior in newEvent.behaviors])

# TODO: Learn Flask-SQLAlchemy. http://flask-sqlalchemy.pocoo.org/2.1/quickstart/
# Some sample functions:
#   model.DogEvent.query.all() <- all events
#   model.DogEvent.query.filter_by(visitor='james').all() <- all my visits
#   model.DogEvent.query.filter_by(ate=1).all() <- all visits where the dog ate