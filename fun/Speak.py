import pyttsx3
import datetime
engine = pyttsx3.init()
voices = engine.getProperty('voices')       
engine.setProperty('voice', 'english')   
engine.setProperty('rate',180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour<12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour<17:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis. Your personal A.I assistant.")

