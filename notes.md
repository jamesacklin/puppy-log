Goals:

- [x] 1. Write a new DogEvent() to a file based on some hard-coded values.
- [x] 2. Read the last entry to the file back to me.
- [x] 3. Write a new DogEvent() to a file with command-line arguments.
- [x] 4. Write a new DogEvent() to a database with command-line arguments.
- [ ] 5. Read the last databse entry back to me.
- [ ] 6. Tell me the last time the dog went on a walk using a database.
- [ ] 7. Learn something about Flask and write a web front-end for this.
- [ ] 8. Write a Flask-API and talk to the application that way.


Hoopes suggested to consider a DogEvent instance to be a single behavior
even if she does 3 things at once, make 3 events with the same timestamp

```
id | time  | visitor | type
1  | 12:00 | "James" | "pee"
2  | 12:00 | "James" | "poop"
3  | 12:05 | "Mary"  | "played"
4  | 12:05 | "Mary"  | "ate
```

This is for SQLAlchemy, but the point is making a set of events based on a for loop

```
for b in ["pee", "poop", "ate"]:
   evt = DogEvent(visitor="James", type=b)
   puppy_app.session.add(evt)
puppy_app.session.commit()  # into the db they go
```

Or even more clever...

```
things = ['pee', 'poop', 'ate']
evts = [DogEvent(visitor='James', type=b) for b in things]
```

Look into Flask-SQLAlchemy at some point.
http://flask-sqlalchemy.pocoo.org/2.1/quickstart/

Some sample functions:
`model.DogEvent.query.all()` <- all events
`model.DogEvent.query.filter_by(visitor='james').all()` <- all my visits
`model.DogEvent.query.filter_by(ate=1).all()` <- all visits where the dog ate
