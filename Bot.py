import telebot
from config import TOKEN
from user import User
import logging

bot = telebot.TeleBot(TOKEN);

@bot.message_handler(commands=['start'])
def sendWelcomMessage(message):
    bot.send_message(message.chat.id, "Для продолжение введите свою группу ")

@bot.message_handler(content_types=["text"])
def getNumberGroup(message):
    msg = bot.send_message(message.chat.id, "Спасибо!")
    user = User(msg)
    user.getNumberGroup(message.text)
    bot.send_message(message.chat.id, user.toString())

bot.polling(none_stop=True)