import requests
import re

API_KEY = "b6048e5226fce6aa183819af"
BASE_URL = "https://v6.exchangerate-api.com/v6"

def extract_currency(user_input):
    user_input = user_input.lower()

    replacements = {
        "india": "INR",
    "usa": "USD",
    "america": "USD",
    "canada": "CAD",
    "uk": "GBP",
    "britain": "GBP",
    "china": "CNY",
    "japan": "JPY",
    "australia": "AUD",
    "new zealand": "NZD",
    "switzerland": "CHF",
    "russia": "RUB",
    "singapore": "SGD",
    "south korea": "KRW",
    "uae": "AED",
    "saudi arabia": "SAR",
    "qatar": "QAR",
    "kuwait": "KWD",
    "europe": "EUR",
    "germany": "EUR",
    "france": "EUR",
    "italy": "EUR",
    "spain": "EUR",
    "netherlands": "EUR"
    }

    for key, value in replacements.items():
        user_input = user_input.replace(key, value)
    match = re.search(r"([A-Za-z]{3})\s*to\s*([A-Za-z]{3})", user_input)

    if match:
        return match.group(1).upper(), match.group(2).upper()

    return None, None

# -----------------------------
# Get LIVE exchange rate
# -----------------------------
def get_rate(from_currency, to_currency):
    url = f"{BASE_URL}/{API_KEY}/pair/{from_currency}/{to_currency}"

    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        return data["conversion_rate"]
    else:
        return None


# -----------------------------
# Main function you will call in chatbot
# -----------------------------
def currency_bot(user_input):
    from_currency, to_currency = extract_currency(user_input)

    if not from_currency or not to_currency:
        return None

    rate = get_rate(from_currency, to_currency)

    if rate:
        return f"1 {from_currency} = {rate} {to_currency}"
    else:
        return "Sorry, I can't fetch exchange rate right now."