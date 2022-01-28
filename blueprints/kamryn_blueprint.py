from flask import render_template, request
from flask import Blueprint
import math
import random
nextAnswerString=""

kamryn_blueprint = Blueprint('kamryn_blueprint', __name__)

@kamryn_blueprint.route('/kamryn_abt/', methods=['GET'])
def kamryn_abt():
    #if request.form:
    #name = request.form.get("name")
    #if len(name) != 0:
    #return render_template("kamryn_abt.html", name=name)
    #, methods=['GET']
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
                      'I am not sure',
                      'Most likely',
                      'You may rely on it']

    randIdx = int(math.floor(random.random()*len(arrayOfAnswers)))
    nextAnswerString = arrayOfAnswers[randIdx]
    return render_template("kamryn_abt.html", currentAnswer=answerString)


#@kamryn_blueprint.route('/reminders/', methods=['GET'])
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

#@kamryn_blueprint.route('/reminders/', methods=['POST'])
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


@kamryn_blueprint.route('/flashcards/')
def flashcards():
    return render_template("flashcards.html")


@kamryn_blueprint.route('/study_break/')
def study_break():
    return render_template("study_break.html")