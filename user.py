import telebot
import logging

class User():
    def __init__(self, message):
        self.id = message.chat.id
        self.name = message.chat.first_name
        self.surname = message.chat.last_name
        self.number = 0
    def     toString(self):
        user = "Id: " + str(self.id) + "\n" \
               "Name: " + str(self.name) + "\n" \
               "Surname: " + str(self.surname) +"\n" \
               "Group: " + str(self.number) + "\n"
        return user
    def getNumberGroup(self, number):
        self.number = number
