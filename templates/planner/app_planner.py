"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from templates.planner.plannersql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_planner = Blueprint('planner', __name__,
                     url_prefix='/planner',
                     template_folder='templates/planner/',
                     static_folder='static',
                     static_url_path='static')

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes for CRUD (Blueprint)
"""


# Default URL
@app_planner.route('/')
def planner():
    """obtains all Users from table and loads Admin Form"""
    return render_template("planner.html", table=assignments_all())


# CRUD create/add
@app_planner.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Assignments(
            request.form.get("name"),
            request.form.get("classname"),
            request.form.get("duedate"),
            request.form.get("notes")
        )
        po.create()
    return redirect(url_for('planner.planner'))


# CRUD read
@app_planner.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        assignmentid = request.form.get("assignmentid")
        po = assignment_by_id(assignmentid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("planner.html", table=table)


# CRUD update
@app_planner.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        assignmentid = request.form.get("assignmentid")
        name = request.form.get("name")
        po = assignment_by_id(assignmentid)
        if po is not None:
            po.update(name)
    return redirect(url_for('planner.planner'))


# CRUD delete
@app_planner.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        assignmentid = request.form.get("assignmentid")
        po = assignment_by_id(assignmentid)
        if po is not None:
            po.delete()
    return redirect(url_for('planner.planner'))


# Search Form
@app_planner.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("plannersearch.html")


# Search request and response
@app_planner.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(assignments_ilike(term)), 200)
    return response