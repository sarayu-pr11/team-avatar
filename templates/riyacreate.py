import time
import random

# list of phrases user may get
typeQuotes= [
    "Oprah Winfrey : Be thankful for what you have; you'll end up having more. If you concentrate on what you don't have, you will never, ever have enough. ",
    "Oscar Wilde : Be yourself; everyone else is already taken.",
    "Albert Einstein : Two things are infinite: the universe and human stupidity; and I'm not sure about the universe",
    "Niccolo Machiavelli: God is not willing to do everything, and thus take away our free will and that share of glory which belongs to us",
    "John Locke: It is one thing to show a man that he is in error, and another to put him in possession of truth",
    "Ralph Waldo Emerson: To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
    "Antoine de Saint-Exupery: Well, I must endure the presence of a few caterpillars if I wish to become acquainted with the butterflies.",
    "Mahatma Gandhi: Live as if you were to die tomorrow. Learn as if you were to live forever.",
    "Aristotle: Those who educate children well are more to be honored than they who produce them; for these only gave them life, those the art of living well.",
    "G B Shaw: The reasonable man adapts himself to the world: the unreasonable one persists in trying to adapt the world to himself. Therefore all progress depends on the unreasonable man.",
    "Ayn Rand: Devotion to the truth is the hallmark of morality; there is no greater, nobler, more heroic form of devotion than the act of a man who assumes the responsibility of thinking.",
    "I am getting better and better as I practice more typing! Hopefully I will be able to improve my typing skills if I keep on practicing",
    "My typing is already top notch! I just like playing this typing game because I want to improve my speed, even though I type pretty accuratley already!",
    "There is a rumour that corgi's backsides are so fluffy that they will float in water. Unfortunatley, no matter how cute this rumor is, it is false!",
    "There are four grades in normal highschool. 9th grade is called freshman, 10th grade is called sophomore, 11th grade is called junior, and 12the grade is called senior"

]

#-----------------------------------------------------------------------------------
# Global Variables: used by both inside functions and outside.
#-----------------------------------------------------------------------------------
quoteList = []
quoteCount = 0
userList = []
userCount = 0
correctList = []
errorList = []
minCount = 0

#-----------------------------------------------------------------------------------
# Starting procedure to get user choice of time or accuracy output
#-----------------------------------------------------------------------------------
def getUserChoice():
    # ask user if they would like to measure their time and words/minute
    print("\n" + "Enter 'T' to measure speed & WPM  OR 'A' to measure accuracy measured" + "\n")

    global startTime
    startTime = time.time()

    userChoice = input()

    global endTime
    endTime = time.time()

    return userChoice

#-----------------------------------------------------------------------------------
# Starting procedure to get user input based on random quote selected !
#-----------------------------------------------------------------------------------
def getUserInput():
    global quoteString
    quoteString = random.choice(typeQuotes)
    print("Type this quote ->", quoteString)

    # user entered their try
    userInputString = input()
    print("User entered string = ", userInputString)

    return userInputString

#-----------------------------------------------------------------------------------
# Function to split quote string and user input string into a list of words
# Function returns the minimum word count between the lists
#-----------------------------------------------------------------------------------
def splitStringsIntoList(userString):

    # get the global list of words in original string by using space as tokenizer
    global quoteList
    global quoteString
    quoteList = quoteString.split(" ")
    # get global word count of the quote string list
    global quoteCount
    quoteCount = len(quoteList)

    # get the global list of words in user string using space as tokenizer
    global userList
    userList = userString.split(" ")
    # User entered string =  Oprah Winfrey : Be thankful for what you have; you'l end up having more.
    # userString =  ['Oprah', 'Winfrey', ':', 'Be', 'thankful', 'for', 'what', 'you', 'have;', "you'l", 'end', 'up', 'having', 'more.']

    #assign global variable to the user  string word count
    global userCount
    userCount = len(userList)

    #get the minumum of word count between quote provided and User entry
    minWordCount = quoteCount

    #check if minCount is greater than userCount and if so, assign userCount to minCount
    if minWordCount > userCount:
        minWordCount = userCount

    return minWordCount

#-----------------------------------------------------------------------------------
# Function to compare the quote word list to the user word list
#-----------------------------------------------------------------------------------
def compareQuoteToUserString(userInputString, metricChoice):

    # call procedure to split strings based on space tokens
    global minCount
    minCount = splitStringsIntoList(userInputString)

    # loop through quoteSplit list and userSplit list and compare each word in it
    # loopIndex is the incremental counter to execute the loop
    # compare words in quoteList to user list to check for errors,  using the loopIndex as the array element index
    #after comparison, we go to the second word by increasing loopIndex
    #we stop the loop when loopIndex == minCount

    #global variables accessed in function
    global correctList
    global errorList
    global typingSpeed
    global userCount
    global quoteCount

    #local variables
    loopIndex = 0
    errorScore = 0

    if metricChoice == 'T':
        #calculate time it took for user input
        timeTaken = endTime - startTime
        return timeTaken
    else:
        while loopIndex < minCount:
            if quoteList[loopIndex] == userList[loopIndex]:
                correctList.append(userList[loopIndex])
            else:
                print("Error! : ", userList[loopIndex], " : at word# =>", loopIndex)
                errorScore = errorScore + 1
                errorList.append(userList[loopIndex])
            loopIndex += 1
        return errorScore

#-----------------------------------------------------------------------------------
# Calculate scores for correct  words
#-----------------------------------------------------------------------------------
def displayCorrectScore(errorScore):
    correctScore = minCount - errorScore
    print("# Matches = ", correctScore," : Words Matched = ", correctList)
    return correctScore

#-----------------------------------------------------------------------------------
# Calculate scores for incorrect words
#-----------------------------------------------------------------------------------
def displayErrorList(errorScore):
    print("# of Errors = ", errorScore, " : Words Not Matched = ", errorList)

#-----------------------------------------------------------------------------------
# Calculate percentage scores for correct and incorrect words
#-----------------------------------------------------------------------------------
def calculatePercentages(wordScore, isCorrect):
    percentScore = wordScore/minCount * 100
    if isCorrect == True:
        print("Accuracy score = ", percentScore, "%")
    else:
        print("Error score = ", percentScore, "%")

#-----------------------------------------------------------------------------------
# Call procedures sequentially
#-----------------------------------------------------------------------------------

while True:
    quoteList = []
    quoteCount = 0
    userList = []
    userCount = 0
    correctList = []
    errorList = []
    minCount = 0

    # ask user what to measure  - accuracy vs speed
    #0  get user response
    metricChoice = getUserChoice()

    # go back to the start of while loop if A or T is not entered
    if metricChoice != 'A' and metricChoice != 'T':
        print("Incorrect User input - please enter choice again")
        continue

    # 1: get user input
    userString = getUserInput()

    # 2: compare the words in the quote list and user list. Returns timeTaken if  T was selected
    # else returns # of incorrect words if A was selected
    userScore = compareQuoteToUserString(userString, metricChoice)

    #Based on user's choice of what to measure, display the appropriate scores.
    if metricChoice == 'A':
        # 3. display error score
        displayErrorList(userScore)
        calculatePercentages(userScore, False)

        # 4. display correct score
        correctCount = displayCorrectScore(userScore)
        calculatePercentages(correctCount, True)
    else:
        #calculate the speed of typing - total words in reference quote over user time taken
        wordsPerMinute = quoteCount/userScore
        print("\n" + "Time Taken = ", userScore, "Words/Minute = ", wordsPerMinute)



