# import random
# from random import *
# from random import shuffle
# a = random.random()
# # print(a)
# b = random.randint(1,100)
# # print(b)
# c = ['arsen', 'john', 'bob', 'mars', 'alex', 'bakai']
# print(random.choice(c))
# c = ['arsen', 'john', 'bob', 'mars', 'alex', 'bakai']
# print(choice(c))
# print(randint(1,100))
# a = [23,56,78,34,56,78,90,34]
# print(sample(a,4))
# random.shuffle(c)
# print(c)

# a = random.randrange(1,100,5)
# print(a)

# from time import sleep

# c = ['arsen', 'john', 'bob', 'mars', 'alex', 'bakai']

# for i in c:
#     print(i)
#     sleep(2)


# from datetime import datetime, time

# now = datetime.now()
# print(now)

# timeobj = time(8,1,45)
# print(timeobj)
# timeobj2 = time(8,1,0)
# print(timeobj2)

# start = datetime.now()

# for i in range(1,100000):
#     print(i)
# end = datetime.now()

# print(end-start)

# print(datetime.today().strftime('%d-%m-%y %H:%M:%S'))

# from random import randint
# a = [randint(0,10) for i in range(20)]
# print(len(a))

# import calendar
# c = calendar.TextCalendar()
# print(c.formatyear(2023))


# import os
# os.mkdir('hello')

# os.rmdir('hello')

# os.system('clear')
# os.system('touch run.py')


# from math import pi, factorial
# a = pi
# print(factorial(5))
# import math
# print(math.cos(20))

# from string import ascii_letters
# from random import choice
# from time import sleep

# while True:

#     password = ''
#     while len(password) < 8:
#         l = choice(ascii_letters)
#         password += l

#     print(password)
#     sleep(0.8)

from random import choice, randint, sample, shuffle, randrange

a = [1,2,3,4,5,6,7,8,9]
# print(choice(a))
# print(sample(a, 4))
# shuffle(a)
# print(a)
# print(randint(50,100))
# print(randrange(0,100,10))

# from datetime import datetime
# a = datetime.now()
# print(a)
# print(datetime.today().strftime('%d-%m-%y %H:%M:%S'))
# team1 = ['agil', 'azamat', 'dias']
# team2 = ['tajibay', 'nazgul', 'dair']
# team3 = ['aidai', 'olga', 'husan']



# import datetime

# current_date = datetime.datetime.now()
# current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')
# print(current_date_string)


# from datetime import datetime
# d_date = {
#     '1': 'января',
#     '2': 'февраля',
#     '3': 'марта',
#     '4': 'апреля',
#     '5': 'мая',
#     '6': 'июня',
#     '7': 'июля',
#     '8': 'августа',
#     '9': 'сентября',
#     '10': 'октября',
#     '11': 'ноября',
#     '12': 'декабря',
# }

# dict1 = {}

# yo = (input("Введите ваш год рождения в формате ДД/MM/ГГГГ: "))
# user_date = datetime.strptime(yo, "%d %m %Y")
# month = user_date.month
# print(f'Вы родились в {user_date:%Y} году, {user_date.day} {d_date[str(month)]}')

# yo = (input("Введите ваш год рождения в формате ДД/MM/ГГГГ: "))
# print(datetime.strptime('%Y', yo))



city = ['Bishkek', 'Osh', 'Batken', 'NewYork']

commands = input('''Выберите действие:
1. Добавить 
2. Отобразить
3. Заменить город \n>>> ''').lower()
if commands == 'добавить':
    new_city = input('Введите название города: ')
    if new_city in city:
        print('Такой город уже есть')
    else:
        city.append(new_city)
elif commands == 'отобразить':
    print(city)






