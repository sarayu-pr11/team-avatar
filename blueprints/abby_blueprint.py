
from flask import render_template, request
from flask import Blueprint
import math
import random

abby_blueprint = Blueprint('abby_blueprint', __name__)



@abby_blueprint.route('/abby_abt/')
def abby_abt():

    #url = "https://inspiring-quotes.p.rapidapi.com/random"

    #querystring = {"author":"Albert"}

    url = "https://inspiring-quotes.p.rapidapi.com/random"

    headers = {
            'x-rapidapi-host': "inspiring-quotes.p.rapidapi.com",
            'x-rapidapi-key': "692ad9b14amshb54be9475d7b493p19b81cjsn4142bd317cb3"
    }

    response = requests.request("GET", url, headers=headers)

    #response = requests.request("GET", url, headers=headers, params=querystring)

    print(response)
    #response.text
    return render_template("abby_abt.html", quotes=response.json())




import requests

url = "https://inspiring-quotes.p.rapidapi.com/random"

querystring = {"author":"Albert"}

headers = {
    'x-rapidapi-host': "inspiring-quotes.p.rapidapi.com",
    'x-rapidapi-key': "692ad9b14amshb54be9475d7b493p19b81cjsn4142bd317cb3"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)