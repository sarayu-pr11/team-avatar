from __init__ import db
from templates.planner.plannermodel import Assignments
import random


# this is method called by frontend, it has been randomized between Alchemy and Native SQL for fun
def assignments_all():
    table = assignments_all_alc()
    return table


# SQLAlchemy extract all users from database
def assignments_all_alc():
    table = Assignments.query.all()
    json_ready = [peep.read() for peep in table]
    return json_ready


# Native SQL extract all users from database
def assignments_all_sql():
    table = db.session.execute('select * from assignments')
    json_ready = sqlquery_2_list(table)
    return json_ready


# SQLAlchemy extract users from database matching term
def assignments_ilike(term):
    """filter Users table by term into JSON list (ordered by User.name)"""
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Assignments.query.order_by(Assignments.name).filter((Assignments.name.ilike(term))
                                                                | (Assignments.classname.ilike(term))
                                                                | (Assignments.duedate.ilike(term))
                                                                | (Assignments.notes.ilike(term)))
    return [peep.read() for peep in table]


# SQLAlchemy extract single user from database matching ID
def assignment_by_id(assignmentid):
    """finds User in table matching userid """
    return Assignments.query.filter_by(assignmentID=assignmentid).first()


# SQLAlchemy extract single user from database matching email
def assignment_by_classname(classname):
    """finds User in table matching email """
    return Assignments.query.filter_by(classname=classname).first()



# ALGORITHM to convert the results of an SQL Query to a JSON ready format in Python
def sqlquery_2_list(rows):
    out_list = []
    keys = rows.keys()  # "Keys" are the columns of the sql query
    for values in rows:  # "Values" are rows within the SQL database
        row_dictionary = {}
        for i in range(len(keys)):  # This loop lines up K, V pairs, same as JSON style
            row_dictionary[keys[i]] = values[i]
        row_dictionary["query"] = "by_sql"  # This is for fun a little watermark
        out_list.append(row_dictionary)  # Finally we have a out_list row
    return out_list


# Test queries
if __name__ == "__main__":
    for i in range(10):
        print(assignments_all())