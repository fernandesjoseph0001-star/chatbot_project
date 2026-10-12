import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()