#!/usr/bin/python
import datetime
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from table_def import Visit

engine = create_engine('sqlite:///visits.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Creating a new event and logging it
def logEvent(time, visitor, behavior):
    newEvent = Visit(time, visitor, behavior)
    session.add(newEvent)
    session.commit()

# Reading from the command line
def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Action can be either 'log' or 'display'", nargs='?')
    parser.add_argument("-v", "--visitor", help="The name of the person who visited the dog.")
    parser.add_argument("-b", "--behavior", help="Things the dog did, in the past tense.", nargs='+')
    args = parser.parse_args()
    if args.action == "log":
        if args.visitor and args.behavior:
            for behavior in args.behavior:
                logEvent(datetime.datetime.now(), args.visitor, behavior)
                print "Time, visitor, and behavior logged."
    if args.action == "display":

        # TODO: Figure out how to do SQLAlchemy's filter operation. I want to
        # AND across options and OR between them. For example:
        # `display -v Mary -b peed pooped` should give me all the
        # events where Mary visited the dog and the dog peed or pooped.
        # For right now, it accepts one, or the other, and ORs them correctly,
        # but does not AND both.

        # if args.visitor and args.behavior:
        #     # for visit in session.query(Visit).filter(or_(visitor == v, behavior == b)).all():
        #     #     displayVisit(visit.behavior, visit.visitor, visit.time)
        #     exit()
        if args.behavior:
            for behavior in args.behavior:
                b = behavior
                for visit in session.query(Visit).filter_by(behavior=b).all():
                    displayEvent(visit.behavior, visit.visitor, visit.time)
            exit()
        if args.visitor:
            v = args.visitor
            for visit in session.query(Visit).filter_by(visitor=v).all():
                displayEvent(visit.behavior, visit.visitor, visit.time)
            exit()
        for visit in session.query(Visit).all():
            displayEvent(visit.behavior, visit.visitor, visit.time)

def displayEvent(behavior, visitor, time):
    print "The puppy %s when %s visited the puppy on %s at %s" % (behavior, visitor, time.strftime("%A, %B %d, %Y"), time.strftime("%I:%M %p"))

if __name__ == "__main__":
    parseArgs()
