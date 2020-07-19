import os

name_file = input("[?]Имя файла:")
name_site = input("[?]Имя сайта:")
login = input("[?]Логин:")
password = input("[?]Пароль:")
dop = input("[?]Доп.:")

full = 'Сайт: ' + name_site + '\r' + 'Логин: ' + login + '\r' + 'Пароль: ' + password + '\r' + 'Дополнить: ' + dop

file = open(name_file, 'w')
file.write(full)
file.close()