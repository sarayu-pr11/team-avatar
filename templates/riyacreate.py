import time
import random

# list of phrases user may get
typeQuotes= [
    "Oprah Winfrey : Be thankful for what you have; you'll end up having more. If you concentrate on what you don't have, you will never, ever have enough. ",
    "Oscar Wilde : Be yourself; everyone else is already taken.",
    "Albert Einstein : Two things are infinite: the universe and human stupidity; and I'm not sure about the universe",
    "Mahatma Gandhi: Live as if you were to die tomorrow. Learn as if you were to live forever.",
    "I am getting better and better as I practice more typing! Hopefully I will be able to improve my typing skills if I keep on practicing for the next few years",
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
correctList = []
errorList = []
minCount = 0

#-----------------------------------------------------------------------------------
# Starting procedure to get user input based on random quote selected
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
def compareQuoteToUserString(userInputString):

    # call procedure to split strings based on space tokens
    global minCount
    minCount = splitStringsIntoList(userInputString)

    # loop through quoteSplit list and userSplit list and compare each word in it
    # loopIndex is the incremental counter to execute the loop
    # compare words in quoteList to user list to check for errors,  using the loopIndex as the array element index
    #after comparison, we go to the second word by increasing loopIndex
    #we stop the loop when loopIndex == minCount
    global correctList
    global errorList
    loopIndex = 0
    errorScore = 0

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
def displayErrorScore(errorScore):
    print("# Errors = ", errorScore, " : Words Not Matched = ", errorList)

#-----------------------------------------------------------------------------------
# Calculate percentage scores for correct and incorrect words
#-----------------------------------------------------------------------------------
def calculatePercentages(wordScore, isCorrect):
    percentScore = wordScore/minCount * 100
    if isCorrect == True:
        print("Correct percentage score = ", percentScore, "%")
    else:
        print("Error percentage score = ", percentScore, "%")

#-----------------------------------------------------------------------------------
# Call procedures sequentially
#-----------------------------------------------------------------------------------

# Call all procedures to compare the strings
# 1: get user input
userString = getUserInput()

# 2: compare the words in the quote list and user list. Enter correct string
errorCount = compareQuoteToUserString(userString)

# 3. display error score
displayErrorScore(errorCount)
calculatePercentages(errorCount, False)

# 4. display correct score
correctCount = displayCorrectScore(errorCount)
calculatePercentages(correctCount, True)



