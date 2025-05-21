from flask import Flask
import threading
import telebot

TOKEN = "7605281790:AAHhl2iUFuv0vtO4GvCsU3JQ5gQ5ED8wyx4"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Приветствие
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """
👋 Приветствуем тебя в JarvisXBot!

🎯 Здесь ты получаешь сигналы по **легендарным стратегиям Lucky Jet** — созданным на опыте, математике и анализе.

🎰 **Ссылка на 1win**: [НАЧАТЬ ИГРАТЬ](https://goo.su/qnkvtL)  
💰 **Промокод:** `FXX86` — получи бонус на депозит!

⚡️ Просто следуй сигналам, делай ставки — и зарабатывай.  
🧠 Наш бот обучается, анализирует и совершенствуется с каждой минутой.

Удачи, чемпион!  
— Твой Джарвис
""", parse_mode="Markdown")

# Web server for keeping bot alive
@app.route('/')
def home():
    return "JarvisXBot is alive!"

# Запуск бота в отдельном потоке
def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)

