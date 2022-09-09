

# lst = ['nurdik', 'alisher', 'eliza', 'agil', 'azamat', 'dair', 'nazgul', 'tajibay', 'bekmamat', 'aidai', 'dias', 'olga', 'husan']
          #0           #1        #2        #3        #4         #5           #6             #7          #8         #9      #10       #11       #12                            
# a = [1,2,3,4,5,6,7,8,9,10]
# start stop step
# print(lst[:])
# print(lst[0:6:1])
# print(a[4:])
# print(a[:3])
# print(a[0:5])
# print(a[1:8:2])                               #-2           #-1
# print(a[0:7:2])
# print(a[::2])
# print(a[:-5:-1])
# print(a[2], a[6], a[-6])
# print(a[2:7])
# a = 'Hello python'
# print(a[:])

# str1 = ['hello', 'python', 'love', 'i']
# print(str1[0], str1[3], str1[2], str1[1])



# a = ['azat', 'alex', 'bakai', 'john', 'akyl','akyl','akyl','akyl',]

# a.append('beka')#добавляет элемент в конец списка
# a.append('bob')
# a.append('nik')
# a.append('abrakadabra')
# name = input('Введи имя: ')
# a.append(name)
# print(a)

a = ['azat', 'alex', 'bakai', 'john', 'akyl','akyl','akyl','akyl']
# print(a)
# a.remove('akyl') # удаляет элемент по названию
# print(a)
# a.pop(2)#удаляет элемент по индексу
# print(a)
# print(a.index('akyl'))
# a.pop(4)
# print(a)

# b = a.count('akyl')# cчитает заданные элементы
# print(a.count('akyl'))

# a = 'asdasdasdasd'
# print(a.count('a'))


# lst1 = ['bael', 'bael','bael','bael','bael','bael','bael']

# lst2 = ['aktan', 'kanykei', 'kanat', 'egdira', 'rimuru','nik']


# lst1.extend(lst2)#обьеденяет два списка
# print(lst1)

# print(len(lst1)) # возвращает длину списка

# len1 = len(lst2)
# l = len1 // 2
# # print(l)
# mid = lst2[0:l]
# print(mid)


# names = []
# name1 = input('Enter name 1: ')
# name2 = input('Enter name 2: ')
# name3 = input('Enter name 3: ')
# name4 = input('Enter name 4: ')
# name5 = input('Enter name 5: ')

# names.append((name1, name2, name3,name4,name5))
# names.extend([name1,name2,name3,name4,name5])
# print(names)

# names = ['nurdik', 'alisher', 'eliza', 'agil', 'dair']
# print(names)

# name = input('Введите имя для удаления: ')
# if name in names:
#     names.remove(name)
# else:
#     print(f'В списке нету имени: {name}')
# print(names)


# names = [('Maga', 40), ('Sultan', 18)]

# name = input('Введите имя: ')
# age = int(input('Введите возраст: '))
# names.append((name,age))
# print(names)



names = ['aktan', 'kanykei', 'kanat', 'egdira', 'rimuru', 'bael', 'nik']
# text = '123455678'
# text = list(text)
# print(text)
# name = len(names) // 2
# print(names[:name])
# print(names[:len(names)//2])
# print(names.index('kanat'))
# print(names[-2:-5:-1])

# a = list(range(0, 100, 4))
# print(a)
# [96,76,56,36,16]
# print(a)
# a = [1,2,3,4,5,6,7,8,9,10]
# a.reverse()#разворачивает наш список

# a = []
# b = input('Введите имя: ')
# a.append(b)
# print(a)

# c = ('alex', 'john', 'bob')
# d = list(c)
# e = tuple(d)
# print(e)


lst1 = ['alex', 'john', 'bob','bakai', 'azat', 'cholpon']
lst2 = ['bakai', 'azat', 'cholpon']
# lst2.extend(lst1)
# print(lst2)
# a = lst1.index('bob')
# lst1.pop(2)
# print(len(lst1))
# print(lst1[::-1])
# start = int(input('Введите старт: '))
# stop = int(input('Введите стоп: '))
# step = int(input('Введите шаг: '))

# if step == 0:
#     print('Шаг не может быть нулём')
# else:
#     lst = list(range(start,stop+1,step))
#     print(lst)



# Создать список вложить в него 5 кортежей
# Создать список из 5 элементов и вывести их по индексу
# Создать список их 5 имен и вывести их через запятую без квадратных скобок
a = [1,'строка',True,[1,2,3], [1,2,3,4]]