import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os
import webbrowser
import pyautogui
import pyjokes



en=pyttsx3.init()
voices = en.getProperty('voices')
en.setProperty('voice' , voices[1].id)


def speak(audio):
    en.say(audio)

    en.runAndWait()

speak("hey boss this is ron and I am ai assistant")
speak('how can i help you')
def time():
    '''returns time in 24 hrs format'''
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("time in 24 hours format is")
    speak(Time)

def date():
    '''returns year , month and day'''
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the year is")
    speak(year)
    speak("the month is")
    speak(month)
    speak("the day is")
    speak(date)

def wishme():
    '''greets the user'''
    speak("hey boss!  hope you are doing well")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("good morning")
    elif hour>=12 and hour <15:
        speak('good afternoon')
    elif hour>=20 and hour <24:
        speak("good evening")
    else:
        speak("good night")
    speak("ron at your service , tell me how can i help you")

def takecommand():
    '''takes user voice as input'''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio , language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again boss")
        return "none"
    return query

def send_email(to , content):
    '''to send email..NOTE: enter you credentials in login and sendmail'''
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.eclo()
    server.starttls()
    server.login('mail', 'password')
    server.sendmail('receiver mail' , 'to' , 'content')
    server.close()

def screenshot():
    '''takes screenshot'''
    img = pyautogui.screenshot()
    img.save('d:\\projects only\\projects\\AI assistant')
    speak('done boss')

def jokes():
    '''returns a joke'''
    joke = pyjokes.get_joke()
    speak(joke)


while 1:
    query = takecommand().lower()

    if "hello" or 'hi' or 'how are you' in query:
        wishme()
    elif 'time' in query:
        time()
    elif 'date' in query:
        date()

    elif "wikipedia" in query:
        speak("boss i am searching")
        query = query.replace("wikipedia" , "")
        result = wikipedia.summary(query , sentences= 2)
        print("ron:" , result)
        speak(result)
    elif 'send mail' in query:
        try:
            speak("what should i write")
            content = takecommand()
            to  = 'kumarronitnov26@gmail.com'
            send_email(to , content)
            speak("email sent succesfully")
        except Exception as e:
            print(e)
            speak('couldnt send due to bad connection')
    elif 'google' in query:
        webbrowser.open_new('www.google.com')

    elif 'youtube' in query:
        webbrowser.open_new('www.youtube.com')

    elif 'instagram' in query:
        webbrowser.open_new('www.instagram.com')

    elif 'github' in query:
        webbrowser.open_new('www.github.com')

    elif 'shut down' in query:
        os.system("shutdown /s /t 1")

    elif 'joke' in query:
        jokes()

    elif 'screenshot' in query:
        screenshot()

    elif 'logout ' in query:
        os.system("shutdown -I")

    elif 'playsong ' in query:
        song_dir = "D:\\favourites"
        songs = os.listdir(song_dir)
    elif 'offline' in query:
        speak("yep done")
        quit()
    else:
        speak('i dont know how to help you boss')

