'''
if True:
    print('Hello')
'''
'''
a = 10
b = 5
if a < b:
    print(True)
else:
    print(False)
'''

'''
a = input('Выберите язык: EN RU KG: ')
if a == 'EN':
    print('Hello')
elif a == 'RU':
    print('Привет')
elif a == 'KG':
    print('Салам')
else:
    print('Такого языка нет')
'''
'''
a = 40
b = 20
c = 10
if a == b and a > c:
    print('Yes')
else:
    print('No')
'''

'''
b = 3 ** 2
a = 2 ** 3
if a > b:
    print('a > b')
else:
    print('b > a')
'''

'''
age = int(input('Введите ваш возраст: '))
if age < 18 and age > 12:
    print('Вы подросток, вам нельзя')
elif age >= 18:
   print('Вы совершеннолетний,входите')
else:
    print('Вы ребенок')
'''
'''
login = input('Введите ваш логин: ')
password = int(input('Введите пароль: '))
password2 = int(input('Повторите пароль: '))

if password == password2:
    print('Пароли совпадают')
    print('Ваш логин: ', login, 'Ваш пароль: ', password)
elif password != password2:
    print('Пароли не совпадают')
'''

'''
num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
if num1 == num2:
    print('ЧИсла равны')
elif num1 > num2:
    print(num1, '>', num2)
elif num1 < num2:
    print(num1, '<', num2)
'''
'''
a = input('Выберите действие: + - / *: ')
num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

if a == '+':
    print(num1 + num2)
elif a == '-':
    print(num1 - num2)
elif a == '/':
    if num2 == 0:
        print('Вы ввели ноль')
    else:
        print(num1 / num2)
elif a == '*':
    print(num1 * num2)
else:
    print('Wrong command')
'''
'''
a = int(input('Введи число: '))
if a % 2 == 0:
    print('Число четное')
else:
    print('Не четное')


'''
'''
a = 10
b = 55
c = 7
if a > b or b < c:
    print(True)
else:
    print(False) 

'''
'''
a = int(input("Enter number: "))


if a > 0 and a <= 21 or a >= 57 and a <= 100:
	print('Число разрешено', a)
else:
	print('Запрещено',a)
'''

a = int(input('Enter num: '))
if a % 2 == 0:
	print('Четное')
else:
	print('Не четное')
if a % 3 == 0:
	print(True)
else:
	print(False)
if a ** 2 > 1000:
	print(True)
else:
	print(False)
