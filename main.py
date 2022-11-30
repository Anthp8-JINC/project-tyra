import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hi, my name is Secret, your personal therapy device. How are you feeling today?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def command_input():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'secret' in command:                              ## Blanks out the commanded word
                command = command.replace('secret', '')
                print(command)



    except:
        pass
    return command

## Takes command by the user
def run_secret():                                               ## Takes command by the user
    command = command_input()
    print(command)


## FEELINGS Conversation

#######  SAD #####
    if 'sad' in command: 
        talk('Oh No! Can I play a song to help cheer you up?')



## Plays the Song and/or Artist Name
    elif 'play' in command:                                       ## Plays the Song and/or Artist Name
        song = command.replace('play', '')
        talk('playing' + song)                                  
        pywhatkit.playonyt(song)



## Gives the current time
    elif 'time' in command:                                     ## Gives the current time
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)                     
        print(time)


## Wikipedia search on a person
    elif 'who is ' in command:                                   ## Wikipedia search on a person
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


## Tell You A Joke
    elif 'joke' in command:                                     ## Tell You A Joke
        talk(pyjokes.get_joke())



## Simple Conversation
    elif 'hello' in command:                                    ## Simple Conversation                          
        talk('Hi!')
    elif 'how are you' in command:
        talk('I am extremely well, thanks for asking!')


## CLOSE THE CONVERSATION ##
    elif 'bye' in command:   
        talk('ok talk to you soon.')                                  
        quit


    else:
        talk("I didn't quite get that, can you say it again?")


        ## Have it return to the "def command_input(): after giving the user the time"

while True:
    run_secret()