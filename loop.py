# Циклы - for, while

# a = ['dias', 'nazgul', 'nurdik', 'dair', 'alisher', ' olga', 'tajibay']
# for i in a:
#     if i == 'dias':
#         print('Ok')
#     else:
#         print('Дальше другие имена')


# for i in range(1,10):
#     a = i * 5
#     print(a)


# a = []
# b = int(input('ВВеди число: '))
# for i in range(b):
#     a.append(i)
# print(a)

# count = 0
from re import I


a = [1,2,3,4,5,5,5,5,5,5,5,6,7,8,9]
# for i in a:
#     if i == 5:
#         count += 1
# print(count)


# count = 0
# for i in a:
#     if i == 4:
#         print('Наша i хранит в себе 4')
#     else:
#         count += 1
# print(count)


# for i in range(1,11):
#     b = 5
#     c = b * i
#     print(f'{b} * {i} = {c}')

# a = ['bishkek', 'naryn', 'osh', 'talas', 'kant', 'batken']
# b = int(input('Введи число: '))
# for i in range(len(a)):
#     if b == i:
#         print(a[i])


# a = ['bishkek', 'naryn', 'osh', 'talas', 'kant', 'batken']
# for i in a:
#     if i == 'kant':
#         a.remove(i)
#         a.append('karakol')
# print(a)

# i = 0
# while i < 10:
#     print(i)
#     i += 1


# count = 1
# a = int(input('Введи число: '))
# while a != 1:
#    print('Repeat')
#    count += 1
#    a = int(input('Введи число: '))
# print(f'Вы потратили {count} попыток')


# a = [1,2,3]*5
# print(a)
# while 3 in a:
#     a.remove(3)
#     print(a)

# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)


# lst = ['Alice', 'Bob', ' Carl', 'Dave']
# x = 'Chris'
# i = 2
# lst[i] = x
# print(lst)

# for i in 'hello python':
#     print(i*2, end='')

# lst = ['Alice', 'Bob', ' Carl', 'Dave']
# a = tuple(lst)
# print(a)

# for i in 'hello world':
#     if i == 'h':
#         continue
#     elif i == 'w':
#         continue
#     print(i, end='')


# a = 0
# while a < 5:
#     a += 1
#     if a == 3:
#         break
#     print(a)


# while True:
#     a = int(input('n= '))
#     if len(str(a)) != 3:
#         print('No')
#     else:
#         print('Yes')
#         break


# b = 'hello world'
# for i in enumerate(b):
#     print(i)

# guess = input('enter password: ')
# password = 'qwerty'
# count = 0
# while guess != password:
#     count += 1
#     print('Wrong password')
#     guess = input('enter password: ')
# print(f'Вы потратили {count} попыток')
    
# count = 0
# a = [1,2,3,4,5,6,7,8,9]
# for i in a:
#    count += 1
# print(count)

# name = []


# for i in range(10):
#     b = input('Добавь имя')
#     name.append(b)
# print(name)
# a = input('>>> ')
# name = ['azat','bakai', 'john', 'tom',2,567,13,32]
# letters = []
# numbers = []
# for i in name:
#     if type(i) == str:
#         letters.append(i)
#     else:
#         numbers.append(i)
# print(letters)
# print(numbers)



a = []
b = []
c = []

for i in range(1,10+1):
    a.append(i)
    if i == 10:
        continue
    b.append(i)
b.reverse()
a.extend(b)
print(*a, sep=',')