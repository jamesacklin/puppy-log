#!/usr/bin/python
import datetime
import cPickle as pickle

# Define event class
class dogEvent(object):
    def __init__(self, time, visitor, behaviors):
        self.time = time
        self.visitor = visitor
        # LOL at the thought of storing JSON in MySQL at some point
        self.behaviors = behaviors

# Write a new DogEvent() to a file based on some hard-coded values.
newEvent = dogEvent(datetime.datetime.now(), "James", ["peed", "pooped", "ate", "bit me", "played"])

# Today we learn about serialization
pickle.dump(newEvent, open('log.txt','wb'))
storedEvent = pickle.load( open( "log.txt", "rb" ) )

# Begin output
print "%s visited the puppy on %s at %s" % (storedEvent.visitor, storedEvent.time.strftime("%A, %B %d, %Y"), storedEvent.time.strftime("%I:%M %p"))
print "The puppy " + ', '.join([str(behavior) for behavior in storedEvent.behaviors])

# Goals:
# 1. Write a new DogEvent() to a file based on some hard-coded values.
# 2. Read the last entry to the file back to me.
# 3. Write a new DogEvent() to a file with command-line arguments.
# 4. Write a new DogEvent() to a database with command-line arguments.
# 5. Read the last databse entry back to me.
# 6. Tell me the last time the dog went on a walk using a database.
# 7. Learn something about Flask and write a web front-end for this.
# 8. Write a Flask-API and talk to the application that way.

# I've decided it's probably a stretch goal to learn SQLAlchemy and
# Flask-SQLAlchemy. Whatever, life is a work.
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/
# Some sample functions:
#   model.DogEvent.query.all() <- all events
#   model.DogEvent.query.filter_by(visitor='james').all() <- all my visits
#   model.DogEvent.query.filter_by(ate=1).all() <- all visits where the dog ate