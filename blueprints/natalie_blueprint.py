from flask import render_template, request
from flask import Blueprint
import math
import random
nextAnswerString=""

natalie_blueprint = Blueprint('natalie_blueprint', __name__)

@natalie_blueprint.route('/natalie_abt/')
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

@natalie_blueprint.route('/calculator/')
def calculator():
    return render_template("calculator.html")

@natalie_blueprint.route('/hwtimer/')
def hwtimer():
    return render_template("hwtimer.html")

