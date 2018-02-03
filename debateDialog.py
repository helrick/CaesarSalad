'''
script that takes user input (in form of voice)
and decides what debate topic to use?

'''
 
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import random
from mutagen.mp3 import MP3

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
    playAudio('\nHello, welcome to debate bot.\nWhat would you like to argue about? I can argue about ' + categoryString)  
    #get input from the user via speech
    categorySelection = ''
    while categorySelection not in TOPICS:
        categorySelection = recordAudio()
        if categorySelection not in TOPICS:
            playAudio('Please enter a valid topic from the following list:')
            print(TOPICS)
    return categorySelection

def startDebate(question):
    print("\n" + question)
    userStance = ''
    while userStance not in ["yes", "y", "no", "n"]:
        playAudio('pick a side, and we can begin.')
        userStance = recordAudio()

def playAudio(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.play()
    audio = MP3("audio.mp3")
    print(audio.info.length)
    
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
    
def echo(data):
    playAudio(data)


main()


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