import telebot
import logging

TOKEN = "413055169:AAEFwg2vGyprcAWzGE5x1gXhyHeZxCLHGhk"
bot = telebot.TeleBot(TOKEN);

@bot.message_handler(commands=['start'])
def sendWelcomMessage(message):
    pass

bot.polling()