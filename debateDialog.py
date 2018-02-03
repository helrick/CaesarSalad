'''
script that takes user input (in form of voice)
and decides what debate topic to use?




'''


TOPICS = ['science', 'law', 'philosophy', 'culture']
DEBATES = {'science': ["should we colonize mars?", "should we use nuclear energy?", "are humans the main cause of global warming?"],'law': ["should cannabis be legal?", "should capital punishment be legal?", "should animal testing be legal?"], 'philosophy': ["does god exist?", "do humans have free will?", "does everything happen for a reason?"], 'culture': ["should we go vegan?", "is capitalism sustainable?", "was nine eleven an inside job?"]}


def main():
    
    quit = False;

    while not quit:
        #should say this:
        topicString = ''
        for t in TOPICS[:-1]:
            topicString.append(t)
        topicString.append('or ' + TOPICS[:-1])


        print('Hello, welcome to debate bot. What would you like to argue about? I can argue about ' + topicString)
        #get input from the user via speech
        topicSelection = raw_input()
        if topicSelection in TOPICS:
            print('From the topic ', topicSelection + 'would you like to debate')
            for d in DEBATES[:-1]:
                print(d)
            print('or ' + DEBATES[:-1])
            debateSelection = raw_input()
            

    







def chooseTopic(userInput):

