import telebot
from telebot import types
from flask import Flask
from threading import Thread
import os

# --- НАСТРОЙКИ ---
TOKEN = '8383397332:AAHs2s0CUJN_cdJQYlfOuaNGr6UKJo8qUu8'
REF_LINK = 'https://t.me/obhod_mobilniy_bot?start=ref_7650109118'

bot = telebot.TeleBot(TOKEN)
app = Flask('')

# --- КНОПКА ---
def get_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Перейти в FastCon", url=REF_LINK)
    markup.add(btn)
    return markup

# --- ОТВЕТ НА ВСЁ ---
@bot.message_handler(func=lambda message: True)
def redirect_all(message):
    text = "Привет! Это переходник на бота VPN FastCon, вот он:"
    bot.send_message(message.chat.id, text, reply_markup=get_keyboard())

# --- СЕРВЕР ДЛЯ РЕНДЕРА ---
@app.route('/')
def home():
    return "Бот работает!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_po
    lling()
