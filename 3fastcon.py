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

# --- ВЕБ-СЕРВЕР ДЛЯ ПИНГА (ЧТОБЫ НЕ СПАЛ НА ХОСТИНГЕ) ---
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

# --- ЛОГИКА БОТА ---
@bot.message_handler(commands=['start'])
def start_message(message):
    # Создаем кнопку-ссылку
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Перейти в FastCon", url=REF_LINK)
    markup.add(btn)
    
    # Текст сообщения
    text = "Привет! Это переходник на бота VPN FastCon, вот он:"
    
    # Отправка сообщения
    bot.send_message(message.chat.id, text, reply_markup=markup)

# --- ЗАПУСК ---
if __name__ == "__main__":
    print("--- Попытка запуска бота ---")
    try:
        keep_alive() 
        print("Статус: Мини-сервер запущен.")
        print("Статус: Бот начал опрос Telegram (Polling)...")
        print("ЗАЙДИ В ТЕЛЕГРАМ И НАПИШИ /start")
        bot.infinity_polling(timeout=60, long_polling_timeout=5)
    except Exception as e:
        print(f"ОШИБКА: {e}")
