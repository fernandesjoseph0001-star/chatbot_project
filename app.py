# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import datetime
# import pyjokes
# from main import get_word_meaning, get_weather, get_news, currency_bot
# import random
# app = Flask(__name__)
# CORS(app)
# @app.route('/chat', methods=['POST'])
# def chat():

#     data = request.get_json()

#     if not data:
#         return jsonify({"reply": "No data received."})

#     message = data.get("message", "").lower().strip()


#     # Dictionary
#     if message.startswith("meaning of"):
#         word = message.replace("meaning of", "").strip()

#         if not word:
#             return jsonify({"reply": "Please type: meaning of <word>"})

#         return jsonify({"reply": get_word_meaning(word)})

#     if message.startswith("define"):
#         word = message.replace("define", "").strip()

#         if not word:
#             return jsonify({"reply": "Please type: define <word>"})

#         return jsonify({"reply": get_word_meaning(word)})

#     # Weather
#     if message.startswith("weather in") or message.startswith("temp in"):
#         city = message.replace("weather in", "").strip()

#         if not city:
#             return jsonify({"reply": "Please type: weather in <city>"})

#         return jsonify({"reply": get_weather(city)})

#     # Joke
#     if "joke" in message:
#         return jsonify({"reply": pyjokes.get_joke()})

#     # Time
#     if "time" in message:
#         current_time = datetime.datetime.now().strftime("%I:%M %p")     
#         return jsonify({"reply": f"Current time is {current_time}"})

#     # Date
#     if "date" in message:
#         current_date = datetime.datetime.now().strftime("%d %B %Y")
#         return jsonify({"reply": f"Today's date is {current_date}"})

#     # News
#     if "news" in message:
#         return jsonify({"reply": get_news()})
    
#     # Currency
#     if message.startswith("currency"):
#         return jsonify({"reply": currency_bot(message)})
 
#     # Greetings
#     if message in ["hi", "hello", "hey"]:
#         return jsonify({"reply": get_response("greeting")})

#     return jsonify({"reply": "Sorry, I didn't understand that."})

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import pyjokes
import random
from main import get_word_meaning, get_weather, get_news, currency_bot
from data.responses import responses

app = Flask(__name__)
CORS(app)


# ── Route ─────────────────────────────────────────────────────────────────────
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data:
        return jsonify({"reply": "No data received."})

    raw_message = data.get("message", "").strip()
    message = raw_message.lower()

    if not message:
        return jsonify({"reply": "Please type something!"})

    # ── Dictionary ────────────────────────────────────────────────────────────
    for prefix in ("meaning of", "define"):
        if message.startswith(prefix):
            word = message.replace(prefix, "", 1).strip()
            if not word:
                return jsonify({"reply": f"Please type: {prefix} <word>"})
            return jsonify({"reply": get_word_meaning(word)})

    # ── Weather ───────────────────────────────────────────────────────────────
    for prefix in ("weather in", "temp in"):
        if message.startswith(prefix):
            city = message.replace(prefix, "", 1).strip()
            if not city:
                return jsonify({"reply": f"Please type: {prefix} <city>"})
            return jsonify({"reply": get_weather(city)})

    # ── Currency ──────────────────────────────────────────────────────────────
    if message.startswith("currency"):
        return jsonify({"reply": currency_bot(message)})

    # ── Jokes ─────────────────────────────────────────────────────────────────
    if "joke" in message:
        return jsonify({"reply": pyjokes.get_joke()})

    # ── Time ──────────────────────────────────────────────────────────────────
    if "time" in message:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return jsonify({"reply": f"Current time is {current_time}."})

    # ── Date ──────────────────────────────────────────────────────────────────
    if "date" in message:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        return jsonify({"reply": f"Today's date is {current_date}."})

    # ── News ──────────────────────────────────────────────────────────────────
    if "news" in message:
        return jsonify({"reply": get_news()})

    # ── Greetings & other responses ───────────────────────────────────────────
    if message in ("hi", "hello", "hey"):
        return jsonify({"reply": random.choice(responses["greeting"])})

    if message in ("bye", "goodbye"):
        return jsonify({"reply": random.choice(responses["bye"])})

    # ── Check all other response keys ─────────────────────────────────────────
    for key, replies in responses.items():
        if key in message:
            return jsonify({"reply": random.choice(replies)})

    # ── Fallback ──────────────────────────────────────────────────────────────
    return jsonify({"reply": "Sorry, I didn't understand that. Try asking for the weather, a joke, the news, or a word definition."})


if __name__ == "__main__":
    app.run(debug=True)