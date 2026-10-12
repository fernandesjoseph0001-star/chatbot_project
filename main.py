import random
import pyjokes
import datetime

from news import get_news
from data.responses import responses
from data.intents import intents
from weather import get_weather
from currency import currency_bot
from dictionary import get_word_meaning
from colorama import Fore, Style, init
from pytsx3 import speak
init(autoreset=True)


def chatbot_reply(user_input):
    user_input = user_input.lower().strip()

    # Currency
    currency_response = currency_bot(user_input)
    if currency_response:
        return currency_response

    # Weather
    if user_input.startswith("weather in"):
        city = user_input.replace("weather in", "").strip()
        temp = get_weather(city)
        return f"Weather in {city.title()} is {temp}°C"

    if user_input.startswith("temp in"):
        city = user_input.replace("temp in", "").strip()
        temp = get_weather(city)
        return f"Temperature in {city.title()} is {temp}°C"

    # Dictionary
    if user_input.startswith("meaning of"):
        word = user_input.replace("meaning of", "").strip()

        if not word:
            return "Please type: meaning of <word>"

        return get_word_meaning(word)

    if user_input.startswith("define"):
        word = user_input.replace("define", "").strip()

        if not word:
            return "Please type: define <word>"

        return get_word_meaning(word)

    # Intent Matching
    for intent, words in intents.items():
        if user_input in words:

            if intent == "joke":
                return pyjokes.get_joke()

            elif intent == "time":
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                return f"Current time is {current_time}"

            elif intent == "date":
                current_date = datetime.datetime.now().strftime("%d %B %Y")
                return f"Today's date is {current_date}"

            elif intent == "weather":
                return "Please type: weather in <city>"

            elif intent == "dictionary":
                return "Please type: meaning of <word>"

            elif intent == "news":
                return get_news()

            else:
                return random.choice(responses[intent])

    return "Sorry, I didn't understand that."


if __name__ == "__main__":
    print("Chatbot is running...")
    speak("Hi! How are you?")

    while True:
        user = input("You: ")

        if user.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            speak("Goodbye!")
            break

        reply = chatbot_reply(user)
        print(Fore.CYAN + "Chatbot: " + Style.RESET_ALL + reply)
        speak(reply)