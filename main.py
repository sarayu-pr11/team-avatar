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


from templates.crud.app_crud import app_crud
from templates.crud.app_crud_api import app_crud_api
app.register_blueprint(app_crud_api)
app.register_blueprint(app_crud)

from templates.planner.app_planner import app_planner
from templates.planner.app_planner_api import app_planner_api
app.register_blueprint(app_planner_api)
app.register_blueprint(app_planner)

from blueprints.kamryn_blueprint import kamryn_blueprint
app.register_blueprint(kamryn_blueprint)

from blueprints.abby_blueprint import abby_blueprint
app.register_blueprint(abby_blueprint)

from blueprints.riya_blueprint import riya_blueprint
app.register_blueprint(riya_blueprint)

from blueprints.sarayu_blueprint import sarayu_blueprint
app.register_blueprint(sarayu_blueprint)


from blueprints.natalie_blueprint import natalie_blueprint
app.register_blueprint(natalie_blueprint)

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

@app.route('/wheel/')
def wheel():
    return render_template("wheel.html")

@app.route('/hwtimer/')
def hwtimer():
    return render_template("hwtimer.html")

@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/tips/')
def tips():
    return render_template("tips.html")

@app.route('/extracurricularslist/')
def extracurriculars():
    return render_template("extracurricularslist.html")


#@app.route('/kamryn_abt/', methods=['GET', 'POST'])
#def kamryn_abt():
    #if request.form:
        #name = request.form.get("name")
        #if len(name) != 0:
            #return render_template("kamryn_abt.html", name=name)
    #return render_template("kamryn_abt.html", name="World")







@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

@app.route('/motivation/')
def motivation():
    return render_template("motivational.html")

@app.route('/draw/')
def draw():
    return render_template("draw.html")
@app.route('/dog/')
def dog():
    return render_template("dog.html")

@app.route('/reminder/')
def reminder():
    return render_template("reminder.html")

@app.route('/flashcards/')
def flashcards():
    return render_template("flashcards.html")

@app.route('/tictactoe/')
def tictactoe():
    return render_template("tictactoe.html")

@app.route('/sudoku/')
def sudoku():
    return render_template("sudoku.html")

@app.route('/memory/')
def memory():
    return render_template("memory.html")

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

@app.route('/rewording/', methods=['GET', 'POST'])
def rewording():
    if request.form:
        url = "https://rimedia-paraphraser.p.rapidapi.com/api_paraphrase.php"
        user_text = request.form.get("user_text")
        if len(user_text) != 0:
            querystring = {"text": user_text, "lang":"en"}
            headers = {
                'content-type': "application/x-www-form-urlencoded",
                'x-rapidapi-host': "rimedia-paraphraser.p.rapidapi.com",
                'x-rapidapi-key': "e2d0d1a7efmsh5668be741c711ffp1a3e44jsnfc9e0a91c2b2"
            }
            response = requests.request("POST", url, data=querystring, headers=headers)
            return render_template("rewording.html", results=response.json())
    else:
        return render_template("rewording.html", results="")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/translate/', methods=['GET', 'POST'])
def translate():
    try:
        text = request.form['text']
        target = request.form['target']
    except:
        text = "   "
        target = "es"

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "e2d0d1a7efmsh5668be741c711ffp1a3e44jsnfc9e0a91c2b2"
        }

    # text = request.form['text']
    # target = request.form['target']

    # text = "Sample Text"
    # text = request.form.get('text')
    # target = request.form.get('target')





    # url encode text
    long_list_of_words = text.split(' ')
    url_encoded_text = f"q={'%20'.join(long_list_of_words)}&target={target}"
    payload = url_encoded_text

    response = requests.request("POST", url, data=payload, headers=headers)

    results = json.loads(response.content.decode("utf-8"))
    
    print(response.text)

    if len(text) != 0:
        return render_template("translate.html", headers=headers, results=results, text=text, target=target)

    return render_template("translate.html", headers=headers, results=results, text='Enter Text To Translate', target='es')






# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

