import requests
from flask import Blueprint
from flask import render_template, request

riya_blueprint = Blueprint('riya_blueprint', __name__)




@riya_blueprint.route('/music/')
def music():
    return render_template("music.html")

@riya_blueprint.route('/riya_abt/')
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

@riya_blueprint.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@riya_blueprint.route('/tips/')
def tips():
    return render_template("tips.html")

