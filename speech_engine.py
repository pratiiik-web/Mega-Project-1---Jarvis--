import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Jarvis 🧠:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except Exception as e:
        print("😵 Couldn't understand:", e)
        return "None"
