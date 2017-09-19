import telebot
import  buttons
import logging
from telebot import types
from config import TOKEN
from config import database_name
from user import User
from SQLighter import SQLStudents

bot = telebot.TeleBot(TOKEN);

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Описание")
    db_worker = SQLStudents(database_name)
    if db_worker.chek_database(message.chat.id) == False:
        add_student(message.chat.id)
    db_worker.close()

@bot.message_handler(regexp="KН36Г")
@bot.message_handler(regexp="KН36Е")
@bot.message_handler(regexp="KН36Д")
def student(message):
    msg = bot.send_message(message.chat.id, "Спасибо, " + message.chat.first_name)
    user = User(msg)
    user.getNumberGroup(message.text)
    db_worker = SQLStudents(database_name)
    db_worker.insert_students(user)
    print(db_worker.counts_row())
    db_worker.close()

def add_student(chat_id):
    markup = buttons.button_add_student()
    bot.send_message(chat_id, "Для продолжение введите свою группу ", reply_markup=markup)

@bot.message_handler(regexp="Понедельник")
@bot.message_handler(regexp="Вторник")
@bot.message_handler(regexp="Среда")
@bot.message_handler(regexp="Четверг")
@bot.message_handler(regexp="Пятница")
def timetable(message):
    pass

if __name__ == '__main__':
    bot.polling(none_stop=True)
