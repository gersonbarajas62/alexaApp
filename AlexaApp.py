#importing Libraries
import speech_recognition as sr
import pyttsx3 
 
global commands
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def user_commands(): 
    try:
        with sr.Microphone() as source:
            print("start speaking")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print (command)
    except:
        pass 
    return command 
       
def run_alexa():
    command = user_commands()
    if 'play' in command:
        command = command.replace('play', '')
        print (command)
        engine_talk('playing' +command)
    else:
        engine_talk('I could not hear you')    


run_alexa()             