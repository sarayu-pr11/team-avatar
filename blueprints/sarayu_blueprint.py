import requests
from flask import Blueprint
from flask import render_template, request

sarayu_blueprint = Blueprint('sarayu_blueprint', __name__)


@sarayu_blueprint.route('/quiz/')
def quiz():
    return render_template("sarayu/quiz.html")





@sarayu_blueprint.route('/sarayu_abt/')
def sarayu_abt():
    url = "https://random-facts2.p.rapidapi.com/getfact"

    headers = {
        'x-rapidapi-host': "random-facts2.p.rapidapi.com",
        'x-rapidapi-key': "b581a96906msh6a688955e0452dfp1a1198jsn9c876326a4f3"
    }

    response = requests.request("GET", url, headers=headers)

    #response.text
    return render_template("sarayu/sarayu_abt.html", stats=response.json())


@sarayu_blueprint.route('/wheel/')
def wheel():
    return render_template("sarayu/wheel.html")

@sarayu_blueprint.route('/draw/')
def draw():
    return render_template("sarayu/draw.html")

@sarayu_blueprint.route('/sarayucreatetask')
def sarayucreatetask():
    return render_template("sarayu/sarayucreatetask.html")

