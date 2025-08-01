# news_module.py
import requests
from config import newsapi

def get_news():
    headlines = []
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
    if r.status_code == 200:
        data = r.json()
        articles = data.get('articles', [])
        for article in articles[:5]:
            headlines.append(article['title'])
    return headlines
