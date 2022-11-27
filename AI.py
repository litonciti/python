import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import wikipedia
import webbrowser
from requests import get
import smtplib
import sys
import pyjokes

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice", voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning, its {tt}")

    elif hour >=12 and hour <= 18:
        speak(f"Good Afternoon, its{tt}")

    else:
        speak(f"Good Evening, its {tt}")

    speak("How May I Help you")

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except:
        speak("say that again please")
        return "none"
    return query

#to wish


#to send email
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("YOUR EMAIL ADDRESS","YOUR PASSWORD")
    server.sendmail("YOUR EMAIL ADDRESS", to, content)
    server.close()

if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            webbrowser.open('facebook.com')

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "you can sleep" in query:
            speak("thanks for using me, have a good day")
            sys.exit()

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")