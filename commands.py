import webbrowser
import requests
from musicLibrary import music
from news_module import get_news
from ai_module import aiProcess
from speech_engine import speak
from config import newsapi
import pygame
import threading
import os

# Global flag to keep track of whether pygame is initialized
pygame_initialized = False

def init_pygame():
    global pygame_initialized
    if not pygame_initialized:
        pygame.init()
        pygame.mixer.init()
        pygame_initialized = True

def play_song(song, file_path):
    try:
        init_pygame()
        speak(f"Playing {song}")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except Exception as e:
        speak("Couldn't play the song.")
        print("❌ Error while playing sound:", e)

def processCommand(c):
    c = c.lower().strip().replace("you tube", "youtube")  # Normalize speech misrecognition

    if "open google" in c:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook"

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"

    elif "news" in c:
        try:
            headlines = get_news()
            for title in headlines[:5]:
                speak(title)
            return "Top 5 headlines read out loud."
        except:
            return "Failed to fetch news."

    elif c.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1].strip()
            file_path = music.get(song)
            print(f"🧩 Looking for song: {song}")
            print(f"🎵 Path from dictionary: {file_path}")
            if file_path and os.path.exists(file_path):
                threading.Thread(target=play_song, args=(song, file_path)).start()
                return f"Playing {song}"
            else:
                return "Sorry, that song is not available in your music folder."
        else:
            return "Please say the song name after 'play'."

    elif "stop music" in c or "stop song" in c or c.strip() == "stop":
        try:
            init_pygame()
            pygame.mixer.music.stop()
            return "Music stopped."
        except Exception as e:
            print("❌ Error stopping music:", e)
            return "Couldn't stop the music."

    else:
        return aiProcess(c)
