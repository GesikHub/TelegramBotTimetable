import telebot
from telebot import types

def button_add_student():
    markup = types.ReplyKeyboardMarkup()
    itembtnG = types.KeyboardButton('KН36Г')
    itembtnD = types.KeyboardButton('KН36Д')
    itembtnE = types.KeyboardButton('KН36Е')
    markup.row(itembtnG, itembtnD, itembtnE)
    return markup

def button_days():
    markup = types.ReplyKeyboardMarkup()
    itembtnMonday = types.KeyboardButton('Понедельник')
    itembtnTuesday = types.KeyboardButton('Вторник')
    itembtnWednesday = types.KeyboardButton('Среда')
    itembtnThursday = types.KeyboardButton('Четверг')
    itembtnFriday = types.KeyboardButton('Пятница')
    itembtnTimeToSession = types.KeyboardButton('Время до сессии')
    markup.row(itembtnMonday, itembtnTuesday)
    markup.row(itembtnWednesday, itembtnThursday)
    markup.row(itembtnFriday)
    markup.row(itembtnTimeToSession)
    return markup

def button_admin():
    markup = types.ReplyKeyboardMarkup()
    itembtnMonday = types.KeyboardButton('Понедельник')
    itembtnTuesday = types.KeyboardButton('Вторник')
    itembtnWednesday = types.KeyboardButton('Среда')
    itembtnThursday = types.KeyboardButton('Четверг')
    itembtnFriday = types.KeyboardButton('Пятница')
    itembtnSendMessageAll = types.KeyboardButton('Отправить сообщение всем пользователям')
    itembtnActivUsers = types.KeyboardButton('Подписчики')
    itembtnTimeToSession = types.KeyboardButton('Время до сессии')
    markup.row(itembtnMonday, itembtnTuesday)
    markup.row(itembtnWednesday, itembtnThursday)
    markup.row(itembtnFriday)
    markup.row(itembtnSendMessageAll)
    markup.row(itembtnActivUsers)
    markup.row(itembtnTimeToSession)
    return markup

def button_admin_message():
    markup = types.ReplyKeyboardMarkup()
    itembtnSendMessage = types.KeyboardButton('Отправить пост')
    itembtnSeeMessage = types.KeyboardButton('Посмотреть как выглядит пост')
    itembtnKillMessage = types.KeyboardButton('Отменить пост')
    markup.row(itembtnSendMessage)
    markup.row(itembtnSeeMessage)
    markup.row(itembtnKillMessage)
    return markup