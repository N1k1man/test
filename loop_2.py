# while True:
#     name = input('Введите имя: ')
#     print(name)
#     if name == 'хватит':
#         break

# names = ['azat', 'bob', 'john', 'alex', 4,8,10]
# # 1 заменить bob на arsen
# # 2 к 8 прибавить 8
# for i in names:
#     if i == 8:
#         names[names.index(i)] += 8
# print(names)





# c=[]
# while True:
#     try:
#         b=input('chislo:\n>>')
#         a=int(b)
#         if type(a)==int:
#             c.append(int(b))
#     except:
#         break
# print('You entered:',c)
# d=0
# for i in c:
#     d+=i
#     rez=d/len(c)
# print('Total:' ,d)
# print('Average:', rez)

# we = ''
# for i in c:
    # we += str(i) + ', '
    # print(i, end=',')
# print(we)
    
# print(f'Вы ввели: {c[:]}')

# ww = ''
# for i in c:
#     print(','.join(str(i)))

a = []
count = 0
total = 0
while True:
    num = input('enter int >>> ')
    if num == 'end':
        break
    else:
        a.append(num)
        count += 1 
        total += int(num)


print('Вы ввели', ", ".join(a))
print('Вы ввели', total)
print('Вы ввели', count)
