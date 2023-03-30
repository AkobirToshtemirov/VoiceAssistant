import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import ecapture as ec
import wolframalpha
import json
import requests
import pyaudio

print('Loading Voice Assistant lol')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speed of reading
rate = engine.getProperty('rate')   # getting the current rate
# decreasing the rate by 50 words per minute
engine.setProperty('rate', rate-45)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("i didnt hear you, please say that again")
            return "none"
        return statement.lower()


wishMe()

if __name__ == '__main__':
    while True:
        speak("what can i do for you?")
        statement = takeCommand()
        if statement == "none":
            continue

        if any(word in statement for word in ["good bye", "stop", "turn off"]):
            speak('see you later!')
            break

        if 'wikipedia' in statement:
            speak('Searching the wiki')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("according to the wiki")
            speak(results)

        elif any(word in statement for word in ["youtube", "open youtube", "go to youtube"]):
            webbrowser.open_new_tab("https://youtube.com")
            speak("youtube is now open")
            time.sleep(3)

        elif any(word in statement for word in ["google", "open google", "ok google"]):
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("Google Mail is open now")
            time.sleep(5)

        elif 'play music' in statement:
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=bKDdT_nyP54")
            speak("Music is playing on youtube")
            time.sleep(5)

        elif 'telegram' in statement:
            # Use the OS module to open the Telegram Desktop application
            speak("Telegram is opening")
            webbrowser.open_new_tab("https://t.me")
            time.sleep(5)
        elif 'weather' in statement:
            webbrowser.open_new_tab(
                "https://www.accuweather.com/en/uz/sirdaryo/355934/weather-forecast/355934")
            speak("It is sunny and warm. Teperature is 15 gradus celcium!")
            time.sleep(5)
        elif 'biology' in statement:
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=wwqJs3hD8E8")
            speak("Biology lesson is opening on youtube!")
            time.sleep(5)
        elif any(word in statement for word in ["english", "english lesson", "english course", "open english lesson"]):
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=eh3fUYTcmDs")
            speak("English lesson is opening on youtube!")
            time.sleep(5)
        elif any(word in statement for word in ["math", "mathematics", "math lesson", "math course", "open math lesson"]):
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=imgRB5bCPyM")
            speak("Math lesson is opening on youtube!")
            time.sleep(5)
        elif any(word in statement for word in ["chemistry", "chemistry lesson", "chemistry course", "open chemistry lesson"]):
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=oS1ocr552Wk")
            speak("Chemistry lesson is opening on youtube!")
            time.sleep(5)
        elif any(word in statement for word in ["russian", "russian lesson", "russian course", "open russian lesson"]):
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=wUHzV6BeQlo")
            speak("Russian lesson is opening on youtube!")
            time.sleep(5)
        elif any(word in statement for word in ["creator", "who created", "who created you?", "who is your creator"]):
            webbrowser.open_new_tab(
                "https://t.me/Akobir_Toshtemirov_Blog")
            speak("Akobir Toshtemirov. Here is his Telegram channel!")
            time.sleep(5)
