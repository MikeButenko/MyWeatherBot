import telebot
import mytoken
from weather import get_weather

token = mytoken.token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, get_weather())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()