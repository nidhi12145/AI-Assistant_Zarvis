import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import musicLibrary

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "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"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')  


    pygame.mixer.init()

    pygame.mixer.music.load('temp.mp3')

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")    



def aiProcess(command):
    client = OpenAI(
        api_key="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",
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com") 
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music.get(song, "https://youtube.com")  # Added get to prevent errors
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apikey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
    else:
        
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=7, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
