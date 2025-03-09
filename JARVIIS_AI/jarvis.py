import pyttsx3  
import datetime  
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os  
import pyautogui
import psutil  
import pyjokes 
import requests, json  

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)


#change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done mam")


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning mam")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon mam")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening mam")
            else:
                speak("it's Goodnight mam")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon mam")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning mam")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening mam")
            else:
                speak("it's Goodnight mam")
    else:
        speak("it's night mam!")


#welcome function
def wishme():
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning mam!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon mam")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening mam")
    else:
        speak("Goodnight mam")

    speak("Jarvis at your service, Please tell me how can i help you?")


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()


#command by user function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #speak(query)
        #print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query

#sending email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("user-name@xyz.com", "pwd")
    server.sendmail("user-name@xyz.com", to, content)
    server.close()


#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))


#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)


def social_media(command):
    if 'facebook' in command:
        speak("Opening your Facebook")
        wb.open("https://www.facebook.com/")
    elif 'whatsapp' in command:
        speak("Opening your WhatsApp")
        wb.open("https://web.whatsapp.com/")
    elif 'discord' in command:
        speak("Opening your Discord server")
        wb.open("https://discord.com/")
    elif 'instagram' in command:
        speak("Opening your Instagram")
        wb.open("https://www.instagram.com/")
    elif 'youtube' in command:
        speak("Opening your youtube")
        wb.open("https://www.youtube.com/")
    else:
        speak("No result found")

def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week


def schedule():
    day = cal_day().lower()
    speak("Mam, today's schedule is as follows:")

    week = {
        "monday": "Mam, from 08:50 AM to 09:40 AM you have Maths - MTB 105, "
                  "from 10:00 AM to 10:50 AM you have CS Lab, "
                  "from 10:50 AM to 11:40 AM you have CS - MCA 201, "
                  "from 11:40 AM to 12:30 PM you have CS - LSCB313, "
                  "from 12:40 PM to 01:30 PM you have Maths - MCA 201 (KS), "
                  "from 02:20 PM to 03:10 PM you have Library session, "
                  "and from 03:10 PM to 04:00 PM you have Computer Networks.",

        "tuesday": "Mam, from 08:50 AM to 09:40 AM you have Computer Networks - MCA 201, "
                   "from 10:00 AM to 10:50 AM you have Library, "
                   "from 10:50 AM to 11:40 AM you have Maths - MOC 001 (CL), "
                   "from 11:40 AM to 12:30 PM you have AI - MCA 202, "
                   "from 01:30 PM to 04:00 PM you have MATLAB.",

        "wednesday": "Mam, from 08:50 AM to 09:40 AM you have AI - MCA 202, "
                     "from 10:50 AM to 11:40 AM you have CS - MCA 201, "
                     "from 11:40 AM to 12:30 PM you have Maths - MCA 201 (CL), "
                     "from 01:30 PM to 02:20 PM you have Library, "
                     "and from 03:10 PM to 04:00 PM you have AI",

        "thursday": "Mam, from 08:50 AM to 09:40 AM you have Maths - GJB 104 (KS), "
                    "from 10:00 AM to 10:50 AM you have CS - MCA 202, "
                    "from 11:40 AM to 12:30 PM you have Maths - AB 305 (VL), "
                    "and from 01:30 PM to 03:10 PM you have CS Lab ",

        "friday": "Mam, from 08:00 AM to 09:40 AM you have SEC, "
                  "from 10:00 AM to 10:50 AM you have AI - MCA 201, "
                  "from 11:40 AM to 12:30 PM you have Maths - MCA 201 "
                  "from 12:40 PM to 01:30 PM you have Computer Networks "
                  "and from 01:30 PM to 04:00 PM you have  Maths Lab.",

        "saturday": "Mam, today you have a more relaxed day with personal projects and self-study.",
        "sunday": "Mam, today is a holiday. Enjoy your free time and relax!"
    }

    if day in week.keys():
        speak(week[day])



def personal():
    speak(
        "I am Jarvis, I am an AI assistant, I am developed by Sindhu and Divanshi"
    )
    speak("Now i hope you know me")


if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

        #time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()

#personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who develop you" in query
              or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

#searching on wikipedia

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

#sending email

        elif ("send email" in query):
            try:
                speak("What is the message for the email")
                content = takeCommand()
                to = 'reciever@xyz.com'
                sendEmail(to, content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak(
                    "Unable to send email check the address of the recipient")
        elif ("search on google" in query or "open website" in query):
            speak("What should i search or open?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

#schedule

        elif ("university time table" in query or "schedule" in query):
            schedule()

#sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

#play songs

        elif ("play songs" in query):
            speak("Playing...")
            songs_dir = "C:\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))
            quit()

#reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

#screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")

#cpu and battery usage
        elif ("cpu and battery" in query or "battery" in query or "cpu" in query):
            cpu()

#jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

#social media
        elif ("facebook" in query or "whatsapp" in query or "discord" in query or "instagram" in query or "youtube" in query):
            social_media(query)


#jarvis features
        elif ("tell me your powers" in query or "help" in query or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("jarvis", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

#exit function

        elif ('i am done' in query or 'bye bye jarvis' in query
              or 'go offline jarvis' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()
