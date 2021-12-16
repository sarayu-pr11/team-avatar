# import "packages" from flask
from flask import Flask, render_template, request, jsonify
import requests


import json
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


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
@app.route('/reminders/')
def reminders():
    return render_template("reminders.html")
@app.route('/hwtimer/')
def hwtimer():
    return render_template("hwtimer.html")

@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/kamryn_abt/')
def kamryn_abt():
    return render_template("kamryn_abt.html", stats=response.json())

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


@app.route('/sarayu_abt/')
def sarayu_abt():
    url = "https://random-facts2.p.rapidapi.com/getfact"

    headers = {
        'x-rapidapi-host': "random-facts2.p.rapidapi.com",
        'x-rapidapi-key': "b581a96906msh6a688955e0452dfp1a1198jsn9c876326a4f3"
    }

    response = requests.request("GET", url, headers=headers)

    #response.text
    return render_template("sarayu_abt.html", stats=response.json())

@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

@app.route('/wheel/')
def wheel():
    return render_template("wheel.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)