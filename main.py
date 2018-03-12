import telebot
import data.buttons
import myString
import os
from datetime import datetime, timedelta
from flask import Flask, request
from config import TOKEN
from config import database_name
from config import admin
from data.user import User
from data.SQLighter import SQLStudents

bot = telebot.TeleBot(TOKEN);
server = Flask(__name__)
check_message = False
admin_mesage = ''
session = datetime(2018, 6, 1, 8, 30, 0, 0)


try:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, myString.start)
        db_worker = SQLStudents(database_name)
        if db_worker.chek_database(message.chat.id) == False:
            add_student(message.chat.id)
        db_worker.close()

    @bot.message_handler(commands=['help'])
    def start_message(message):
        db_worker = SQLStudents(database_name)
        if db_worker.chek_database(message.chat.id) == False:
            add_student(message.chat.id)
        else:
            if message.chat.id in admin:
                bot.send_message(message.chat.id, myString.help_for_admin)
            else:
                bot.send_message(message.chat.id, myString.help_for_users)
        db_worker.close()


    @bot.message_handler(regexp="KН36Г")
    @bot.message_handler(regexp="KН36Е")
    @bot.message_handler(regexp="KН36Д")
    def student(message):
        if message.chat.id in admin:
            markup = data.buttons.button_admin()
        else:
            markup = data.buttons.button_days()
        msg = bot.send_message(message.chat.id, "Спасибо, " + message.chat.first_name, reply_markup=markup)
        user = User()
        user.message(msg)
        user.getNumberGroup(message.text)
        db_worker = SQLStudents(database_name)
        db_worker.insert_students(user)
        db_worker.close()

    @bot.message_handler(regexp="Понедельник")
    @bot.message_handler(commands=['monday'])
    def send_timetable_monday(message):
        db_worker = SQLStudents(database_name)
        if db_worker.chek_database(message.chat.id) == False:
            add_student(message.chat.id)
        else:
            student = db_worker.select_id(message.chat.id)
            bot.send_message(message.chat.id, 'Понедельник\n')
            if student.number == 'KН36Г':
                bot.send_message(message.chat.id, myString.monday_kn36g)
            if student.number == 'KН36Д':
                bot.send_message(message.chat.id, myString.monday_kn36d)
            if student.number == 'KН36Е':
                bot.send_message(message.chat.id, myString.monday_kn36e)
        db_worker.close()

    @bot.message_handler(regexp="Вторник")
    @bot.message_handler(commands=['tuesday'])
    def send_timetable_tuesday(message):
        db_worker = SQLStudents(database_name)
        if db_worker.chek_database(message.chat.id) == False:
            add_student(message.chat.id)
        else:
            student = db_worker.select_id(message.chat.id)
            bot.send_message(message.chat.id, 'Вторник\n')
            if student.number == 'KН36Г':
                bot.send_message(message.chat.id, myString.tuesday_kn36g)
            if student.number == 'KН36Д':
                bot.send_message(message.chat.id, myString.tuesday_kn36d)
            if student.number == 'KН36Е':
                bot.send_message(message.chat.id, myString.tuesday_kn36e)
        db_worker.close()

    @bot.message_handler(regexp="Среда")
    @bot.message_handler(commands=['wednesday'])
    def send_timetable_wednesday(message):
        db_worker = SQLStudents(database_name)
        if db_worker.chek_database(message.chat.id) == False:
            add_student(message.chat.id)
        else:
            student = db_worker.select_id(message.chat.id)
            bot.send_message(message.chat.id, 'Среда\n')
            if student.number == 'KН36Г':
                bot.send_message(message.chat.id, myString.wednesday_kn36g)
            if student.number == 'KН36Д':
                bot.send_message(message.chat.id, myString.wednesday_kn36d)
            if student.number == 'KН36Е':
                bot.send_message(message.chat.id, myString.wednesday_kn36e)
        db_worker.close()

    @bot.message_handler(regexp="Четверг")
    @bot.message_handler(commands=['thursday'])
    def send_timetable_thursday(message):
        db_worker = SQLStudents(database_name)
        if db_worker.chek_database(message.chat.id) == False:
            add_student(message.chat.id)
        else:
            student = db_worker.select_id(message.chat.id)
            bot.send_message(message.chat.id, 'Четверг\n')
            if student.number == 'KН36Г':
                bot.send_message(message.chat.id, myString.thursday_kn36g)
            if student.number == 'KН36Д':
                bot.send_message(message.chat.id, myString.thursday_kn36d)
            if student.number == 'KН36Е':
                bot.send_message(message.chat.id, myString.thursday_kn36e)
        db_worker.close()


    @bot.message_handler(regexp="Пятница")
    @bot.message_handler(commands=['friday'])
    def send_timetable_friday(message):
        db_worker = SQLStudents(database_name)
        if db_worker.chek_database(message.chat.id) == False:
            add_student(message.chat.id)
        else:
            student = db_worker.select_id(message.chat.id)
            bot.send_message(message.chat.id, 'Пятница\n')
            if student.number == 'KН36Г':
                bot.send_message(message.chat.id, myString.friday_kn36g)
            if student.number == 'KН36Д':
                bot.send_message(message.chat.id, myString.friday_kn36d)
            if student.number == 'KН36Е':
                bot.send_message(message.chat.id, myString.friday_kn36e)
        db_worker.close()

    @bot.message_handler(commands=['button'])
    def button(message):
        db_worker = SQLStudents(database_name)
        if db_worker.chek_database(message.chat.id) == False:
            add_student(message.chat.id)
        else:
            if message.chat.id in admin:
                markup = data.buttons.button_admin()
            else:
                markup = data.buttons.button_days()
            bot.send_message(message.chat.id, "Кнопки добавлены", reply_markup=markup)
        db_worker.close()

    @bot.message_handler(regexp="Отправить сообщение всем пользователям")
    @bot.message_handler(commands=['messageall'])
    def send_messageall(message):
        bot.send_message(message.chat.id, 'Введите текст сообщения')
        global check_message
        check_message = True

    @bot.message_handler(regexp="Отправить пост")
    def send_message(message):
        global admin_mesage
        db_worker = SQLStudents(database_name)
        students = db_worker.select_all()
        for student in students:
            bot.send_message(student[0], admin_mesage)
        markup = data.buttons.button_admin()
        bot.send_message(message.chat.id, 'Пост отправлен', reply_markup=markup)
        admin_mesage = '' ''

    @bot.message_handler(regexp='Отменить пост')
    def kill_message(message):
        global admin_mesage
        admin_mesage = ''
        global check_message
        check_message = False
        markup = data.buttons.button_admin()
        bot.send_message(message.chat.id, 'Пост был отменен', reply_markup=markup)

    @bot.message_handler(regexp='Подписчики')
    def counter_users(message):
        db_worker = SQLStudents(database_name)
        bot.send_message(message.chat.id, db_worker.counts_row())
        students = db_worker.select_all()
        for student in students:
            bot.send_message(message.chat.id, str(student[0]) + " " + str(student[1]) + " " + str(student[2]) + " " + str(student[3]))
        db_worker.close()


    @bot.message_handler(commands=['timeexams'])
    @bot.message_handler(regexp='Время до сессии')
    def time_to_session(message):
        difference_time = timedelta(hours=0)
        new_time = session - (datetime.now() + difference_time)
        str_time = list(str(new_time).split())
        for_student = str(new_time.days) + " дней " + str_time[2].split(':')[0] + " часов " \
                      + str_time[2].split(':')[1] + " минут " + \
                      str_time[2].split(':')[2].split('.')[0] + " секунд"
        bot.send_message(message.chat.id, for_student)


    @bot.message_handler(content_types=['text'])
    def set_message(message):
        global check_message
        if (check_message) and (message.chat.id in admin):
            global admin_mesage
            admin_mesage += message.text
            markup = data.buttons.button_admin_message()
            bot.send_message(message.chat.id, 'Пост добавлен', reply_markup=markup)
            check_message = False
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю')


    def add_student(chat_id):
        markup = data.buttons.button_add_student()
        bot.send_message(chat_id, "Для продолжение введите свою группу ", reply_markup=markup)


    @server.route("/439253618:AAEC3C29rePF6ZdREKJfOv32zw3T_TjJPhg", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://bottimetable.herokuapp.com/439253618:AAEC3C29rePF6ZdREKJfOv32zw3T_TjJPhg")
        return "!", 200

    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5001))

except:
    bot.send_message(admin[1], "Я упал, помоги мне")
