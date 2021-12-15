# import "packages" from flask
from flask import Flask, render_template, request, jsonify
import requests

import random
import math
import json

# create a Flask instance
app = Flask(__name__)
nextAnswerString = ""

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


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/kamryn_abt/', methods=['GET'])
def kamryn_abt():
    global nextAnswerString
    answerString = nextAnswerString

    arrayOfAnswers = ['Yes, definitely!',
                      'No, absolutely not.',
                      'Maybe...',
                      'Concentrate and ask',
                      'Unlikely',
                      'Certainly',
                      'Do not count on it',
                      'As I see it, yes',
                      'Ask again later',
                      'I am not sure',
                      'Most likely',
                      'You may rely on it']

    randIdx = int(math.floor(random.random()*len(arrayOfAnswers)))
    nextAnswerString = arrayOfAnswers[randIdx]
    return render_template("kamryn_abt.html", currentAnswer=answerString)

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

       # return render_template("riya_abt.html", data=stats)

@app.route('/natalie_abt/')
def natalie_abt():

    url = "https://numbersapi.p.rapidapi.com/1492/year"
    querystring = {"fragment":"true","json":"true"}
    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "57a15be86bmsh8ab5c9d255b7689p1346f0jsnb3b6bfbfaba4"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    quote = ""
    date = ""
    year = ""
    try:
        quote = json.loads(response.content.decode("utf-8"))['text']
        date = json.loads(response.content.decode("utf-8"))['date']
        year = json.loads(response.content.decode("utf-8"))['number']
    except:
        print ("No date from URL")

    print ("quote  = ", quote)
    print ("date  = ", date)
    print ("year  = ", year)

    r = json.dumps(response.text)
    loaded_r = json.loads(r)

    return render_template("natalie_abt.html", quote=quote, year=year, date=date,
                           r=loaded_r)

@app.route('/abby_abt/')
def abby_abt():
    return render_template("abby_abt.html")


@app.route('/sarayu_abt/')
def sarayu_abt():
    url = "https://random-facts2.p.rapidapi.com/getfact"

    headers = {
        'x-rapidapi-host': "random-facts2.p.rapidapi.com",
        'x-rapidapi-key': "cb6c4ae0c0mshf7c680cd7f9687bp1c11edjsnd948864f5be3"
    }

    response = requests.request("GET", url, headers=headers)

     #response.text
    return render_template("sarayu_abt.html", stats=response.json())

@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

@app.route('/music/')
def page1():
    return render_template("music.html")

@app.route('/hwtimer/')
def hwtimer():
    return render_template("hwtimer.html")

@app.route('/reminders/')
def reminders():
    return render_template("reminders.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
