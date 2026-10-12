import requests

def get_word_meaning(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return f"No meaning found for '{word}'."

        data = response.json()

        definition = data[0]["meanings"][0]["definitions"][0]["definition"]

        return definition

    except Exception as e:
        return f"Error: {e}"