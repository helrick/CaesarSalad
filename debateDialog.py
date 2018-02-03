'''
script that takes user input (in form of voice)
and decides what debate topic to use?

'''

import random

TOPICS = ['science', 'law', 'philosophy', 'culture']
DEBATES = {'science': ["should we colonize mars?", "should we use nuclear energy?", "are humans the main cause of global warming?"],'law': ["should cannabis be legal?", "should capital punishment be legal?", "should animal testing be legal?"], 'philosophy': ["does god exist?", "do humans have free will?", "does everything happen for a reason?"], 'culture': ["should we go vegan?", "is capitalism sustainable?", "was nine eleven an inside job?"]}

def main():

    category = getCategories() 
    question = random.choice(DEBATES[category])
    #use the debate selection to start the debate on that question
    startDebate(question)


# select the topic from which we will select a debate
def getCategories():
    categoryString = ''
    for t in TOPICS[:-1]:
        categoryString += t + ", "
    categoryString += 'or ' + TOPICS[-1] + ":"
    print('\nHello, welcome to debate bot.\nWhat would you like to argue about? I can argue about ' + categoryString)  
    #get input from the user via speech
    categorySelection = ''
    while categorySelection not in TOPICS:
        categorySelection = raw_input()
        if categorySelection not in TOPICS:
            print('Please enter a valid topic from the following list:')
            print(TOPICS)
    return categorySelection

def startDebate(question):
    print("\n" + question + "\n")
    userStance = ''
    while userStance not in ["yes", "y", "no", "n"]:
        userStance = raw_input()



'''
#choose a specific debate question
def selectDebate(topicSelection):
    print("From the topic '" + topicSelection + "' would you like to debate:\n")
    for d in DEBATES[topicSelection]:
        print('"' +  d + '"')
    debateSelection = ''
    while debateSelection not in DEBATES[topicSelection]:
        debateSelection = raw_input()
        if debateSelection not in DEBATES[topicSelection]:
            print('Please enter a valid debate question from the following list:')
            print(DEBATES[topicSelection])
  
    return topicSelection
'''

#first input it category
#then we randomly choose from the available topics in that category
#ask the question to the user, get a 'yes' or a 'no'

main()
