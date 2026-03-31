# commands/news.py
import requests
from config import NEWS_API_KEY
from speech import speak

def get_news():
    url = f"###"
    r = requests.get(url)
    data = r.json()

    if data["status"] != "ok":
        speak("Error fetching news")
        return

    for article in data["articles"][:5]:
        speak(article["title"])