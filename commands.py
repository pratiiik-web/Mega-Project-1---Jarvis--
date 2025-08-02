# commands.py
import webbrowser
import requests
from musicLibrary import music
from news_module import get_news
from ai_module import aiProcess
from speech_engine import speak
from config import newsapi

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        return "Opening Facebook"

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music.get(song)
        if link:
            webbrowser.open(link)
            return f"Playing {song}"
        else:
            return "Sorry, song not found."

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            headlines = [article['title'] for article in articles[:5]]
            for title in headlines:
                speak(title)
            return "Top 5 headlines read out loud."
        else:
            return "Failed to fetch news."

    else:
        output = aiProcess(c)
        return output
