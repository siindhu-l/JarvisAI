import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening......")   
        r.pause_threshold = 1 
        r.energy_threshold = 300  
        audio = r.listen(source,0,4)

    try:
        print("understanding......")
        query = r.recognize_google(audio,language='en-us')
        print(f"You Said : {query}")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("who do you want to message")
    a = input('''person1 - 1
    person2 - 2''')
    if a == 1:
        speak("whats the ,message")
        message = str(input("enter the message- "))
        pywhatkit.sendwhatmsg("+919719077627",message,time_hour = strTime,time_min=update)
    elif a == 2:
        speak("whats the ,message")
        message = str(input("enter the message- "))
        pywhatkit.sendwhatmsg("+919180665369",message,time_hour = strTime,time_min=update)
