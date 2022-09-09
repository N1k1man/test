
'''
string = ''
stin2 = 'Привет'
stin3 = 'пайтон'
s = string + stin2 + 'мир' 
print(s)
'''
'''
print('Привет\n\n\n\n')
'''
'''
print("hello wooooorld".upper())
'''
'''
a = 'привет мир'.upper()
print(a)

b = 'HELLO WORLD'.lower()
print(b)
'''
'''
name = input('Введите ваше имя:').lower()

if name.startswith('a') and name.endswith('n'):
    print('Ваше имя начинается на а и зачанчиваетя на н')
else:
    print('Введи верное имя')
'''


'''
a = 'Hello world'
print(a.endswith('world'))
print(a.startswith('He'))
'''
'''
t = 'asdfg'
text = 'Мир дружба жвачка'.split()
print(len(text))
'''
'''
name = input('Введите ваше имя:')
print(f'Привет {name} тебя приветстует твой код')
'''
'''
text = 'мир труд май'.title()
t = text.capitalize()
print(t)
'''
'''
string = '                              Hello world                  '
print(string.strip())
'''

'''
text = 'мир труд май май май май май май'

t = text.count(' ')
print(t)

text_1 = ' '.join(text)
print(f'{text_1} - данную строку разделили пробелами при помощи join')
'''

'''
text = 'asfghgj'
text_1 = '1234235436'
print(text.isalpha())
print(text_1.isdigit())
'''

'''
a = 'asdasd'

if not a.isdigit() and  not a.isalpha():
    print(True)
else:
    print(False)
'''
'''
login = input('Введите логин: ')
password = input('Введите пароль: ')
password2 = input('Повторите пароль: ')
if not password.isdigit() and not password.isalpha():
    if len(password) == 8 and password == password2:
        print(f'Ваш логин: {login}, пароль: {password}')
    else:
        print('Пароль меньше 8 символов')
else:
    print('Введи пароль заново')

'''

'''
password = input('pass1: ')
password2 = input('pass2: ')
if password.isalpha() or password.isdigit():
    print(f'Пароль должен состоять и из букв и из цифр{password}')

elif len(password) < 8:
    print(f'Пароль {password} должен быть не менее 8 символов')

elif password != password2:
    print(f'Пароли не совпадают: {password} != {password2}')
else:
    print(f'Пароль подходит - {password}')
'''
'''
text = 'hegat'
print(text.replace('gat', 'llo'))
text2 = 'привет'.replace('и', 'e')
print(text2)
'''
'''
a = 123455
print('hello' + 'world' + str(a))
'''


'''
a = True
print(type(a))
b = 123
print(type(b))
c = '123'
print(type(c))
d = int(c)
print(type(d))
'''

'''
a = input('введи имя ')
print(f'ваше имя {a}')
'''

a = 'Github'
b = input('Введи симвоЛ: ')
print(b.join(a))
