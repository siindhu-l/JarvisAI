import pyttsx3
import speech_recognition   
import requests
import datetime
import keyboard
import pyautogui
import webbrowser
import random
from bs4 import BeautifulSoup      


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
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


def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up jarvis" in query:
            from greet_me import greet_me
            greet_me()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:   #listening state
                    speak("Okay, Wake me anytime !")
                    break
                elif "hello" in query:
                    speak("Hello ! How are you ?")
                elif "i am fine" in query:
                    speak(" that's great !")
                elif "how are you" in query:
                    speak("i'm doing great !")
                elif "thank you" in query:
                    speak("your welcome !")


                elif "tired" in query:
                    speak("Playing your favourite songs")
                    a = (1,2,3) # choose any number of songs 
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open() # put the link of the video


                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")


                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()
 

                elif "open" in query:
                    from dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dictapp import closeappweb
                    closeappweb(query)

                    
                elif "google" in query:
                    from search_now import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from search_now import searchYouTube
                    searchYouTube(query)
                elif "wikipedia" in query:
                    from search_now import searchWikipedia 
                    searchWikipedia(query)

                    
                elif "temperature" in query:
                    search = "temperature in banglore"
                    url = "https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", __build_class__ = "BNeaWE").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "temperature in banglore"
                    url = "https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeaWE").text
                    speak(f"current {search} is {temp}")


                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"the time is {strTime}")
                elif "finally sleep" in query: #off mode
                    speak("going to sleep")
                    exit()


                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt","r")
                    speak("You told me to remember that" + remember.read())

