# commands.py
import webbrowser
import requests
from musicLibrary import music
from news_module import get_news
from ai_module import aiProcess
from speech_engine import speak
from config import newsapi

def processCommand(command):
    c = command.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, song not found.")
    elif "news" in c:
        headlines = get_news()
        for title in headlines:
            speak(title)
    else:
        response = aiProcess(command)
        speak(response)
