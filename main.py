# main.py

from commands import processCommand
from speech_engine import take_command, speak
import speech_recognition as sr

def handle_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        response = processCommand(command)
        return command, response
    except Exception as e:
        print("Voice recognition failed:", e)
        return "Voice recognition failed", "Sorry, I couldn't understand."

def handle_text_command(text):
    try:
        print("Processing text command:", text)
        response = processCommand(text)
        return response
    except Exception as e:
        print("Text command error:", e)
        return "Something went wrong while processing your request."
