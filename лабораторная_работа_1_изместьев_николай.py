# -*- coding: utf-8 -*-
"""Лабораторная работа 1 Изместьев Николай.ipynb

**Задание 1**
"""

import re
text = 'В данном случае, моё регулярное (выражение) будет верным... В данном случае, моё регулярное выражение будет верным!'
result = re.finditer(r'([А-Я0-9\-\:\,\;\'\"]\s*)([А-ЯЁа-яё0-9\-\:\,\;\'\"\(\)]+\s*)+[А-ЯЁа-яё0-9\-\,\;\'\"\-\(\)]+(\.{3}|[.?!])\s*', text)
for i in result:
  print(i.group())

"""**Задание 2**"""

text = 'нехорошего человека'
result = re.sub(r'(=?^редис[а-я]+)|(=?^нехорош[а-я]+\sчелове[а-я]+)', '*давайте жить дружно*', text)
print(result)

"""**Задание 3**"""

while (True):
  print("Введите пароль")
  input_string = str(input())
  pattern_password = re.compile(r'(?=.*[A-Z].*)(?=.*[a-z].*)(?=.*[0-9].*)(?=.*[\.\!\?].*)[A-Za-z0-9\.\!\?]{6,}')
  if (bool(pattern_password.match(input_string))):
    print("Вход выполнен")
    break 
  else:
    print('Вход не выполнен, введите правильный пароль')

"""**Задание 4**"""

while (True):
  print("Введите email")
  input_string = str(input())
  email = re.finditer(r'([A-Za-z0-9\_\-]+)\@([A-Za-z]+\.[A-Za-z0-9\_\-\.]+){2,}', input_string)
  if (len(list(email)) != 0):
    print("Email введен корректно")
    break 
  else:
    print('Email введен не правильно, повторите ввод')

"""**Задание 5**"""

import datetime 
date_string = '12.02.1998'
result = re.finditer(r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])\.(?:0?[1-9]|1[0-2])\.(?:19[0-9][0-9]|20[01][0-9])(?!\d)', date_string)
for i in result:
  print(datetime.datetime.strptime(i.group(),'%d.%m.%Y').strftime('%Y-%m-%d'))