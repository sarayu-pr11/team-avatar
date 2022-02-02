""" database dependencies to support Users db examples """
from sqlalchemy.exc import IntegrityError
from __init__ import db

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Assignments(db.Model):
    # define the Users schema
    assignmentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    classname = db.Column(db.String(255), unique=True, nullable=False)
    duedate = db.Column(db.String(255), unique=False, nullable=False)
    notes = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, classname, duedate, notes):
        self.name = name
        self.classname = classname
        self.duedate = duedate
        self.notes = notes

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "assignmentID": self.assignmentID,
            "name": self.name,
            "classname": self.classname,
            "duedate": self.duedate,
            "notes": self.notes,
            "query": "by_alc"  # This is for fun, a little watermark
        }

    # CRUD update: updates users name, duedate, notes
    # returns self
    def update(self, name, duedate="", notes=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(duedate) > 0:
            self.duedate = duedate
        if len(notes) > 0:
            self.notes = notes
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: assignments")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Assignments(name='G6 Homework', classname='Math', duedate='2/3/22', notes="Check Answers")
    u2 = Assignments(name='Study for Test', classname='Chemistry', duedate='None', notes="Khan Academy")
    u3 = Assignments(name='Add Search Bar', classname='Computer Science', duedate='None', notes="Search google")
    u4 = Assignments(name='Homework', classname='Physics', duedate='2/3/22', notes="None")
    u5 = Assignments(name='Finish Worksheet', classname='Spanish', duedate='2/4/22', notes="None")
    u6 = Assignments(name='Egg Drop', classname='Physics', duedate='2/21/22', notes="Must be 8x8x8")
    # U7 intended to fail as duplicate key
    u7 = Assignments(name='Notes', classname='AP Euro', duedate='2/8/22', notes="None")
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.classname}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from assignments')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Assignments
    model_printer()