#!/usr/bin/python
# table_def.py

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///visits.db', echo=False)
Base = declarative_base()

class Visit(Base):
    """"""
    __tablename__ = "visits"
    id = Column(Integer, primary_key=True)
    time = Column(Date)
    visitor = Column(String)
    behavior = Column(String)
    def __init__(self, time, visitor, behavior):
        """"""
        self.time = time
        self.visitor = visitor
        self.behavior = behavior

Base.metadata.create_all(engine)
