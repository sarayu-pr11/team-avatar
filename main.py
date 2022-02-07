# import "packages" from flask
from flask import render_template, request
from __init__ import app
import requests
import os
import pickle
import math
import random
import json
nextAnswerString=""



# create a Flask instance
#app = Flask(__name__)

from blueprints.sarayu_blueprint import sarayu_blueprint
app.register_blueprint(sarayu_blueprint)
from blueprints.kamryn_blueprint import kamryn_blueprint
app.register_blueprint(kamryn_blueprint)
from blueprints.riya_blueprint import riya_blueprint
app.register_blueprint(riya_blueprint)
from templates.crud.app_crud import app_crud
from templates.crud.app_crud_api import app_crud_api
app.register_blueprint(app_crud_api)
app.register_blueprint(app_crud)

from templates.planner.app_planner import app_planner
from templates.planner.app_planner_api import app_planner_api
app.register_blueprint(app_planner_api)
app.register_blueprint(app_planner)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/')
def pali():
    return render_template("palindrome.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/music/')
def music():
    return render_template("music.html")


@app.route('/hwtimer/')
def hwtimer():
    return render_template("hwtimer.html")

@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/tips/')
def tips():
    return render_template("tips.html")

@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/riya_abt/')
def riya_abt():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = "{ \"key1\": \"value\",\"key2\": \"value\"}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
        'x-rapidapi-key': "066e279e11mshd6855dd2ac40d0dp19761ajsn088d1e5fbc92"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    text = response.text
    return render_template("riya_abt.html", results=text)
    #url = "https://covid-19-data.p.rapidapi.com/report/totals"
    # querystring = {"date":"2020-07-21"}
    # headers = {
    #  'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    #    'x-rapidapi-key': "066e279e11mshd6855dd2ac40d0dp19761ajsn088d1e5fbc92"
    #  }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    #stats=[
    #{
    # 'name':'Audrin',
    # 'place': 'kaka',
    # 'mob': '7736'
    # },
    #   {
    #  'name': 'Stuvard',
    # 'place': 'Goa',
    # 'mob' : '546464'
    #  }
    #  ]
    #return(response.text)
    # results = response.text

    #return render_template("riya_abt.html", data=stats)

@app.route('/natalie_abt/')
def natalie_abt():
    #url = "https://numbersapi.p.rapidapi.com/1492/year"
    #querystring = {"fragment":"true","json":"true"}
    #headers = {
    #    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
    #   'x-rapidapi-key': "57a15be86bmsh8ab5c9d255b7689p1346f0jsnb3b6bfbfaba4"
    #}
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #results = json.loads(response.content.decode("utf-8"))['results']
    #year = []
    #for result in results:
    #        # result['year']
    #        year.append(result['year'])
    #    # tournament = json.loads(response.content.decode("utf-8"))['results'][0]['year']

    return render_template("natalie_abt.html")

@app.route('/abby_abt/')
def abby_abt():
    return render_template("abby_abt.html")


@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

@app.route('/motivation/')
def motivation():
    return render_template("motivational.html")

@app.route('/calculator/')
def calculator():
    return render_template("calculator.html")

@app.route('/tictactoe/')
def tictactoe():
    return render_template("tictactoe.html")

@app.route('/sudoku/')
def sudoku():
    return render_template("sudoku.html")

@app.route('/dictionary/', methods=['GET','POST'])
def dictionary():
    try:
        keyword = request.form['keyword']
    except:
        keyword = "study"
    url = "https://twinword-word-graph-dictionary.p.rapidapi.com/definition/"
    querystring = {"entry":keyword}
    headers = {
        'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code<400:
        results = json.loads(response.content.decode("utf-8"))
        return render_template("dictionary.html", results=results, word=keyword)
    else:
        return render_template("dictionary.html", word=keyword)
    # print(response.text)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


