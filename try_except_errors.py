# print()
# input()
# sum()
# min()
# max()
# len()

# a = [5==5, 5 > 7]
# print(all(a))# all - возвращает Тру, если все значения верные

# a = [2,4,6,8,7,6,4,3]
# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(True)
#     else:
#         b.append(False)
# print(all(b))


# a = [2,4,6,8,7,6,4,3]
# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(True)
#     else:
#         b.append(False)

# # any()
# print(any(b)) # Возвращает True, если хоть 1 значение True
# a = [False,False, True]
# print(any(a))

# abs()

# a = -25200
# print(abs(a)) # Возвращает абсолютную величину

# a = [2,4,5,6,7,8,13]
# print(min(a))
# print(max(a))
# print(sum(a))

# a = [2,4,5,6,7,8,13]
# a.reverse()
# print(a)
# eval()
# a = eval('2 + 2')
# print(a)
# a = [2,3,4,5,6]
# check_this = eval(input('Enter your code: '))
# print(check_this)


# while True:
#     a = eval(input('>>> '))
#     print(a)



# slice()

# list1 = ['aktan', 'bektur', 'ron', 'rick', 'angela']
# print(slice(list1, 0, 1))


# a = 10 /3
# print(round(a, 2))#  округляет до выбранного значения


# try:
#     a = int(input('Введите цифру а: '))
#     b = int(input('Введите цифру b: '))
#     print(a/b)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Вводите только цифры')


# try:
#     a = [1,2,3,5,6]
#     print(a[1])
# except IndexError:
#     print('Такого индекса нет')



# try:
#     a = int(input('Введите цифру а: '))
#     b = int(input('Введите цифру b: '))
#     print(a/b)
# except (ZeroDivisionError, NameError, ValueError):
#     print('Поймал все ошибки')
# else:
#     print('Не было ошибок')

# finally:
#     print('Finally')

# try:
#     print('str' / 5)
# except Exception as e:
#     print(f'Код вырубился из-за ошибки: {e}')


# str_1 = 'Python'
# a = slice(2)
# print(str_1[a])


# a = [1,2,3,4,5,6,7,7]
# # try:
# #     dict(a)
# #     print('Yes')
# # except:
# #     print('Так делать нельзя')

# print(set(a))



# a = 0
# b = 1
# numbers = []
# while b > a:
# 	numbers.append(b)
# 	b += 1
# 	break

# print(b)
# print(numbers)



