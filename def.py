# def print_text():
#     print('Hello')

# print_text()

# def sum1():
#     a = 5
#     b = 34
#     return a + b
# print(sum1())

# def sum2(a,b):
#     return a * b

# print(sum2(5, 3))
# print(sum2(3, 20))
# print(sum2(2,15))


# print(len(a))

# def my_len(a:list):
#     s = 0
#     for i in a:
#         s += 1
#     return s
# list1 = [1,2,3,4,5,6,7,8,9]

# list2 = ['a','b', 'c', 'd', 'e', 'f']

# list3 = [1,2,3,4,5,7,8,9,0]
# # my_len(list1)

# print(my_len(list2))
# print(my_len(list3))



# def my_sum(a,b,d):
#     return a + b + d
# print(my_sum(20,10,20))


# def umnozh(a:int, b=10):
#     return f'Вы умножили a на b результат = {a*b} '

# print(umnozh(3))
# print(umnozh(10,7))


# a = ['Bishkek', 'Osh', 'Kant']

# def list_city(a):
#     for i in a:
#         print(i, end=', ')


# def add_city():
#     new_city = input('Введите новый город:')
#     if new_city in a:
#         print('Такой город есть')
#     else:
#         a.append(new_city)
#         print('Город успешно добавлен')
#         list_city(a)
    

# def main_loop():

#     while True:
#         commands = input('Введите комманду: Добавить: отобразить: выход: ')
        
#         if commands == 'добавить':
#             add_city()
            
#         elif commands == 'отобразить':
#             list_city(a)
#         elif commands == 'выход':
#             exit()

# main_loop()



# def print1():
#     print('Функция в функции')

# def summ1(a,b):
#     print1()
#     return a + b

# print(summ1(5, 8))

# def print2():
#     print('Еще функция в функции')

# def text1(a,b):
#     print1()
#     print2()
#     return a - b

# print(text1(10,5))



# def list1(a:list):
#     b = []
#     mid = len(a) //2 
#     c = a[:mid]
#     d = a[mid:]
#     d.reverse()
#     c.reverse()
#     b.extend(c)
#     b.extend(d)
#     return b
# b = ['1','5', 'age', 'name']
# print(list1(b))


# file_name = input('Введите название файла с расщирением .txt:')
# with open(file_name, 'w') as f:
#     f.write('Hello')
#     print(f'Файл с именем {file_name} успешно создан')

def func1(range1):
    b = []
    for i in range(range1):
        c = input('Введи текст: ')
        b.append(c)
    return b

diapazon = int(input('Введи диапазон: '))
a = func1(diapazon)
print(a)