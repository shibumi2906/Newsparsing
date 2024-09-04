import telebot
from telebot import types
from parsing import get_latest_news
from db import get_unshown_news, mark_news_as_shown, all_news_shown
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

# Клавиатура с кнопками
def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Новости"), types.KeyboardButton("Источники"))
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    get_latest_news()  # Парсим новости при старте
    bot.send_message(message.chat.id, "Привет! Я бот, который парсит новости об ИИ.", reply_markup=get_keyboard())

@bot.message_handler(func=lambda message: message.text == "Новости")
def news(message):
    if all_news_shown():  # Проверяем, есть ли еще непоказанные новости
        bot.send_message(message.chat.id, "Новостей больше нет.")
    else:
        news_item = get_unshown_news()  # Получаем следующую новость
        if news_item:
            title, link = news_item
            bot.send_message(message.chat.id, f"Заголовок: {title}\nСсылка: {link}")
            mark_news_as_shown(link)  # Отмечаем новость как показанную

@bot.message_handler(func=lambda message: message.text == "Источники")
def sources(message):
    bot.send_message(message.chat.id, "Источники: TechCrunch, MIT Technology Review, IEEE Spectrum")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Команды: /start, /news, /help")

bot.polling()

