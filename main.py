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
from templates.crud.app_crud import app_crud
from templates.crud.app_crud_api import app_crud_api
app.register_blueprint(app_crud_api)
app.register_blueprint(app_crud)


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


@app.route('/calculator/')
def calculator():
    return render_template("calculator.html")


@app.route('/reminders/', methods=['GET'])
def reminders():
    #kdf = open('/tmp/KammyDebug.txt', 'wt+')
    MAX_NUM_NOTES=8
    fileInfoReminder = [0 for i in range(MAX_NUM_NOTES)]
    attribNames = [0 for i in range(MAX_NUM_NOTES)]
    tmpNotes = ['' for i in range(MAX_NUM_NOTES)]
    #kdf.writelines('in reminders: \n')
    for ii in range(MAX_NUM_NOTES):
        # create file if it doesnt exist.
        try:
            fileInfoReminder[ii] = open('/tmp/fileInfo%d.bin'%ii, 'rb')
        except:
            os.system('touch /tmp/fileInfo%d.bin'%ii)
            fileInfoReminder[ii] = open('/tmp/fileInfo%d.bin'%ii, 'rb')

        try:
            dataDict = pickle.load(fileInfoReminder[ii])
            #kdf.writelines('Reading Notes: %s\n' % dataDict)
            tmpNotes[ii] = dataDict['tmpNote']
        except:
            tmpNotes[ii] = ""
            #kdf.writelines('Error Deleting All Notes')
        #<textarea id="box7" style="margin: 2%" rows="9" cols="32" placeholder="remind me..."></textarea>
        attribNames[ii] = {'idName': "box%d"%(ii+1), 'style': "margin: 50%", 'rows': "9", 'cols':"32", "placeholder":"remind me..."}

    #kdf.close()
    return render_template("reminders.html", attrib_names=attribNames, persistentNotes=tmpNotes, numUpdates=MAX_NUM_NOTES)


@app.route('/reminders/', methods=['POST'])
def storeNotes():
    #kdf = open('/tmp/KammyDebug.txt', 'wt+')
    blob = request.data
    dataDict = json.loads(bytes.decode(blob))
    #kdf.writelines('Storing Notes: %s\n' % dataDict)
    boxIdx = int(dataDict['idName'][3:])-1
    fileInfoStorage = open('/tmp/fileInfo%d.bin'%boxIdx, 'wb+')
    pickle.dump(dataDict, fileInfoStorage)
    #kdf.writelines('Storing Notes: %s\n' % dataDict)
    #kdf.close()
    fileInfoStorage.close()
    attribNames=[]
    return render_template("reminders.html", attrib_names=attribNames, numUpdates=0)



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


