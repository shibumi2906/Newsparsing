import requests
from bs4 import BeautifulSoup
import config
from db import save_news

def get_latest_news():
    for source in config.NEWS_SOURCES:
        response = requests.get(source)
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')[:5]  # Ограничиваем последние 5 новостей
        for item in items:
            title = item.title.text
            link = item.link.text
            description = item.description.text
            news_item = {
                'title': title,
                'summary': description,  # Можно добавить функцию summarize_text для сокращения описания
                'link': link
            }
            save_news(news_item)  # Сохраняем новости в базу данных
