# lst1 = [1,2,3,4,5,6,7,8,9,10]
# Создать список из 10 имен
# импортировать в другой файл 4 рандомных имени в новый список


from string import ascii_letters
from random import choice
from time import sleep

# while True:

#     password = ''
#     while len(password) < 8:
#         l = choice(ascii_letters)
#         password += l

#     print(password)
#     sleep(0.8)

# password = 'QWE'
# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# count = 0




# password = 'QWE'
# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# count = 0

# while True:
#     pass1 = ''
    
#     while len(pass1) < 3:
#         l = choice(letters)
#         pass1 += l
#     if pass1 != password:
#         count +=1
#         print(pass1)

#     else:
#         print(pass1)
#         print(count)
#         break


from string import digits
from random import choice
a = []
while len(a) < 2:
    a.append(choice(digits))
print(a)