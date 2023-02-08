#importing Libraries
import speech_recognition as sr
import pyttsx3 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

engine.say("I am your bot")
engine.say("how can i help you")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("start speaking")
        voice = listener.listener(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print (command)
except:
    pass 