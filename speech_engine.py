# speech_engine.py

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)  # speed of speech
engine.setProperty('volume', 1)  # 0.0 to 1.0

# Optional: change voice (e.g., to female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female (depends on OS)

def speak(text):
    print("Jarvis:", text)  # also print it in console for debugging
    engine.say(text)
    engine.runAndWait()
