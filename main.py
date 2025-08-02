import speech_recognition as sr
from speech_engine import speak
from commands import processCommand

recognizer = sr.Recognizer()

def handle_voice_command():
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        command = recognizer.recognize_google(audio)
        response = processCommand(command)  # should return a string
        speak(response)
        return command, response
    except Exception as e:
        return "Error", str(e)
    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    speak("How can I assist you today?")
    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            wake_word = recognizer.recognize_google(audio)

            if wake_word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)
