import telebot
from telebot import types

def button_add_student():
    markup = types.ReplyKeyboardMarkup()
    itembtnG = types.KeyboardButton('KН36Г')
    itembtnD = types.KeyboardButton('KН36Д')
    itembtnE = types.KeyboardButton('KН36Е')
    markup.row(itembtnG, itembtnD, itembtnE)
    return markup