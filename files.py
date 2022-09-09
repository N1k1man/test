# file = open('names.txt', 'w')
# # file.write('Hello\nnazgul')
# # file.write('nazgul')
# file.write('Privet mir')
# file.close()

# a = ['beka', 'nurdik', 'argen', 'mars', 'asyl']
# file = open('text.txt', 'w')
# for i in a:
#     file.write(f'{i} \n')
# file.close()

# b = ['azat', 'alex', 'ron']
# file = open('text.txt', 'a')
# for i in b:
#     file.write(f'{i} \n')
# file.close()
# file = open('text.txt', 'a')
# for i in range(4):
#     a = input('>>> ')
#     file.write(f'{a} \n')
# file.close()


# with open('text2.txt', 'w') as f:
#     f.write('Good evening')
# with open('text2.txt', 'r') as f:
#     print(f.read())

# with open('login.txt', 'a') as f:
#     login = input("Введите логин: ")
#     f.write('Логин: ')
#     f.write(login)
# print('Успешно создан файл с логином')


# names = ['nazgul', 'husan', 'dias', 'azamat', 'eliza', 'agil', 'tajibay', 'nurdik', 'dair', 'olga', 'aidai']
# with open('names.txt', 'w') as f:
#     for i in names:
#         f.write('\n')
#         f.write(str(names.index(i)))
#         f.write(' ')
#         f.write(i)
# print('Все получилось')


# with open('n.txt', 'w') as f:
#     for i in range(10):
#         b = int(input('Введи число: '))
#         f.write(f'{b} \n')


# a = 'home/lessons1/data/'
# with open('img' ,'w') as f:
#     f.write('data/foto.jpg')


with open('/home/aa/directories.txt', 'r')as f:
    a = f.read()

# with open('text_777.txt', 'w') as f:
#     f.write(a)

print(a)