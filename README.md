# Python Chatbot

This is a Python-based chatbot project. It responds to predefined user messages and includes features such as jokes, date and time, weather information, news headlines, dictionary lookup, currency conversion, and voice output.

## Project Files

- `main.py` — starts the command-line chatbot
- `data/intents.py` — contains the supported user phrases
- `data/responses.py` — contains predefined chatbot responses
- `weather.py` — weather feature
- `news.py` — news headlines feature
- `currency.py` — currency conversion feature
- `dictionary.py` — word-meaning lookup
- `pytsx3.py` — voice output helper
- `database.sql` — SQL database script
- `app.py` — Flask-related project file

## Run the Chatbot

1. Install Python.
2. Open this folder in VS Code.
3. Install the packages required by the project, including `pyjokes`, `requests`, `colorama`, and `pyttsx3`.
4. Run:

   ```bash
   python main.py
   ```

## Notes

Weather, news, and currency conversion depend on their API services and valid API keys. Keep API keys private and do not publish them in a public repository.
