import requests

API_KEY = "50357c12fd020ba1c7b4dcffaba9972b"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code != 200:
        return None

    return round(data["main"]["temp"])
