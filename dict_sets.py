# a = [5,8,4,3,2]
# a.sort()
# print(a)
# print(max(a))
# print(min(a))
# print(sum(a))

# dict1 = {}
# print(type(dict1))

# d = dict(short = 'dict', long = 'dictionary')
# print(d)

# dict1 = {
#      1:2,
#     'str': 'string', 
#     'bool': True,
#     'list': [1,2,3]
# }
# print(dict1)


person = {
    'name': 'Will Smith',
    'age': 30,
    'profession': 'Actor'
}
person['height'] = 180
person['age'] = 40
person['planet'] = 'Mars'
person2 = {'race': 'troll'}
person.update(person2)# обновляет словарь
# person.pop('age')# удаляет элемент по ключу
c = person.get('race') # возвращает значение по ключу
# print(person['name'])# выводит на экран значение по ключу
# print(c)
# print(person)
# person.clear()
# a = person.copy()# создает копию словаря
person.setdefault(7, 'seven')# Создает новую пару ключ:значение, но если такой ключ уже есть, ничего не произойдет
# print(person.values())# возвращает значения
# print(person.keys()) # возвращает ключи
# print(person.items())
# print(person)
# dict1 = {}
# dict1['one'] = [1,2,3]
# dict1['two'] = (4,5,6)
# print(len(dict1))


# for key in person:
#     print(key)

# for value in person.values():
#     print(value, end=', ')

# for key, value in person.items():
#     print(f'{key} = {value}')


# for key in person:
#     if key == 'name':
#         person['name'] = 'Johny Depp'
#     elif key == 'age':
#         person['age'] -= 20

# print(person)


# rooms = {'bathroom', 'dinning-room', 'hall', 'bedroom'}
# print(type(rooms))

# set1 = set()
# a = 10
# c = 'str'
# d = True
# set1.add(a)# добавляет элемент в множество
# set1.add(d)
# set1.add(c)

# print(set1)


# set_1 = {1,2,3,4,4,4,4,4,4,4,5,6,6,6,6,6,6,6,7,8}# множество хранит уникальные данные
# print(set_1)
# set_1.clear()
# set2 = set_1.copy()
# set3 = {5,4,3,6,8,9}
# print(set3)

# set1 = {'bakai', 'nurdik', 'dair', 'mars', 'beka'}
# set2 = {'azat', 'bakai', 'alex', 'beka', 'mars'}
# set3 = set2.difference(set1)# возвращает разницу множеств
# set1.update(set2)
# print(set1)

# a = {1,2,3}
# b = {4,5,6}
# b.update(a)# обьединяет два множества
# b.remove(1)# удаляет элемент по названию
# print(b)

# a = {1,2,3,4,5}
# b = {1,2,3,7,8,9}
# c = a.intersection(b)# Выводит одинаковые данные из множеств
# print(c)

# a = {
#     'number': [4,7,8]
# }

# for value in a.values():
#     print(value[2])


# b = {1,2,3,4,5,6,7,8,9}
# print(type(b))
# c = list(b)
# d = tuple(b)
# print(d)


# dict1 = {
#     '2255339911':{
#         'name': 'Nick',
#         'surname': 'Rog'
#     }
# }


# for key in dict1['2255339911']:
#     for i in key:
#         print(i)
    



# for i in range(1,10):
#     print(i)
#     for j in range(1,10):
      


dict1 = {
    '2244991156': {
        'name': 'Alex', 
        'surname': 'Kawalski', 
        'age': 30, 
        'gender': 'M'
    },
    '111999334':{
        'name': 'John',
        'surname': 'Doe', 
        'age': 40,
        'gender': 'M'
    },
    '449919934':{
        'name': 'Alice',
        'surname': 'Akynova',
        'age': 20,
        'gender': 'F'
    }
}

# print(dict1['449919934']['name'])

# for value in dict1['2244991156'].values():
#     print(value)

# for key, value in dict1.items():
#     print(key, value)

# for value in dict1.values():
#     for i, j  in value.items():
#         print(f'i = {i}, j = {j}')


# list1 = [[1,2,3], [4,5,6], [7,8,9]]
# for i in list1:
#     for j in i:
#         print(j, end=' ')





