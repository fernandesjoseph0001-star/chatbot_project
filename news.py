import requests

API_KEY = "02e0b721354f42658a5b4bf4b25a2e07"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        articles = data["articles"][:5]

        news = "Top Headlines:\n\n"

        for i, article in enumerate(articles, start=1):
            news += f"{i}. {article['title']}\n"

        return news

    return "Unable to fetch news."
