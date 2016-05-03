#!/usr/bin/python
import datetime
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Visit

engine = create_engine('sqlite:///visits.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Creating a new event and logging it
def logEvent(time, visitor, behavior):
    newEvent = Visit(time, visitor, behavior)
    # print "The puppy %s when %s visited the puppy on %s at %s" % (newEvent.behavior, newEvent.visitor, newEvent.time.strftime("%A, %B %d, %Y"), newEvent.time.strftime("%I:%M %p"))
    session.add(newEvent)
    session.commit()

# Reading from the command line
def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--visitor", help="The name of the person who visited the dog.", required=True)
    parser.add_argument("-b", "--behavior", help="Things the dog did, in the past tense.", nargs='+', required=True)
    args = parser.parse_args()
    if args.visitor and args.behavior:
        for behavior in args.behavior:
            logEvent(datetime.datetime.now(), args.visitor, behavior)

if __name__ == "__main__":
    parseArgs()
