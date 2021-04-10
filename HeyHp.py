import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hp' in command:
                command = command.replace('hp','')
    except:
        pass
    return command

def run_command():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        currenttime = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is' + currenttime)
        print(currenttime)

    elif 'tell me something about' in command:
        person = command.replace('tell me something about', '')
        info = wikipedia.summary(person, 1) #1 = one line informtion
        talk(info)
        print(info)

    else:
        talk('Say it again or check your command')

run_command()