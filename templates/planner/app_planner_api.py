"""control dependencies to support CRUD routes and APIs"""
from flask import Blueprint, render_template
from flask_restful import Api, Resource
import requests

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
from templates.planner.plannersql import assignments_all, assignment_by_classname, assignment_by_id, assignments_ilike

app_planner_api = Blueprint('planner_api', __name__,
                         url_prefix='/planner_api',
                         template_folder='templates/planner/',
                         static_folder='static',
                         static_url_path='static')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_planner_api)


# Method #2 for CRUD
@app_planner_api.route('/')
def planner_api():
    """obtains all Users from table and loads Admin Form"""
    return render_template("planner/templates/../planner_async.html", table=assignments_all())


""" API routes section """


class AssignmentsAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, assignmenttype, classname, duedate, notes):
            po = Assignments(assignmenttype, classname, duedate, notes)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {assignmenttype}, either a format error or {classname} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return assignments_all()

    # class for delete
    class _ReadID(Resource):
        def get(self, assignmentid):
            po = assignment_by_id(assignmentid)
            if po is None:
                return {'message': f"{assignmentid} is not found"}, 210
            data = po.read()
            return data

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return assignments_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, classname, assignmenttype):
            po = assignment_by_classname(classname)
            if po is None:
                return {'message': f"{classname} is not found"}, 210
            po.update(assignmenttype)
            return po.read()

        # class for update/put

    class _UpdateAssignmentType(Resource):
        def put(self, assignmentid, assignmenttype):
            po = assignment_by_id(assignmentid)
            if po is not None:
                po.update(assignmenttype)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, classname, assignmenttype, duedate, notes):
            po = assignment_by_classname(classname)
            if po is None:
                return {'message': f"{classname} is not found"}, 210
            po.update(assignmenttype, duedate, notes)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, assignmentid):
            po = assignment_by_id(assignmentid)
            if po is None:
                return {'message': f"{assignmentid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:assignmenttype>/<string:classname>/<string:duedate>/<string:notes>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadID, '/read/<int:assignmentid>')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:classname>/<string:assignmenttype>')
    api.add_resource(_UpdateAssignmentType, '/update/<int:assignmentid>/<string:assignmenttype>')
    api.add_resource(_UpdateAll, '/update/<string:classname>/<string:assignmenttype>/<string:duedate>/<string:notes>')
    api.add_resource(_Delete, '/delete/<int:assignmentid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/planner_api'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/1', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/read/4', "get"],
        ['/delete/5', "delete"],
        ['/read/5', "get"],
        ['/update/1/Thomas Alva Edison', "put"]
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users table")
    for assignment in assignments_all():
        print(assignment)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()