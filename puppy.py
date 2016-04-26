#!/usr/bin/python
import datetime

# Define event class
class DogEvent(object):
    def __init__(self):
        self.time = datetime.datetime.utcnow()

# Instantiate new event
newEvent = DogEvent()
print newEvent.time

# TODO: Learn Flask-SQLAlchemy. http://flask-sqlalchemy.pocoo.org/2.1/quickstart/
# Some sample functions:
#   model.DogEvent.query.all() <- all events
#   model.DogEvent.query.filter_by(visitor='james').all() <- all my visits
#   model.DogEvent.query.filter_by(ate=1).all() <- all visits where the dog ate