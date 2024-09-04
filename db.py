import sqlite3

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS news (title TEXT, link TEXT, shown INTEGER)''')  # Добавлено поле "shown"
    conn.commit()

# Сохранение новости
def save_news(news_item):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO news (title, link, shown) VALUES (?, ?, ?)", (news_item['title'], news_item['link'], 0))
    conn.commit()

# Получение необработанных новостей
def get_unshown_news():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, link FROM news WHERE shown = 0 ORDER BY ROWID ASC LIMIT 1")  # Получаем одну необработанную новость
    result = cursor.fetchone()
    return result

# Обновление статуса новостей как показанных
def mark_news_as_shown(link):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE news SET shown = 1 WHERE link = ?", (link,))
    conn.commit()

# Проверка, все ли новости показаны
def all_news_shown():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM news WHERE shown = 0")  # Считаем непросмотренные новости
    count = cursor.fetchone()[0]
    return count == 0  # Если все новости показаны, возвращаем True

