import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = speech_recognition.Recognizer
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

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on Google ")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No speakable output available")

def searchYouTube(query):
    if "youtube" in query:
        speak("This is what I found for your search !")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("playing")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searching in wikipedia")
        query = query.replace("search wikipedia", "")
        query = query.replace("wikipedia", "")
        query = query.replace("jarvis", "")
        wikipedia.summary(query,sentences=2)
        results = speak("according to wikipedia")
        print(results)
        speak(results)
