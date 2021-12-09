# import "packages" from flask
from flask import Flask, render_template, request
import requests

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


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/kamryn_abt/')
def kamryn_abt():
    return render_template("kamryn_abt.html")

@app.route('/riya_abt/')
def riya_abt():
    return render_template("riya_abt.html")

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
    return render_template("sarayu_abt.html")

@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)