import sqlite3
import os

# Вывод текущей рабочей директории для отладки
print("Текущая рабочая директория:", os.getcwd())

# Получаем путь к директории скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'news.db')

def init_db():
    # Используем явный путь для базы данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            title TEXT,
            link TEXT,
            shown INTEGER
        )
    ''')
    conn.commit()
    print(f"База данных создана в {db_path}")

# Инициализация базы данных
init_db()

