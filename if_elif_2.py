'''
transport = input('Какой вид транспорта вы выбираете: самолет, поезд, автобус: ')

if transport == 'самолет':
    ticket_type = input('Каким классом вы хотите лететь: эконом, бизнес: ')
    if ticket_type == 'эконом':
        place = input('Где вы хотите место: у окна, в проходе: ')
    else:
        place = 'у вас свой зал'

elif transport == 'поезд':
    ticket_type = input('Как вы хотите ехать: плацкарт, купе: ')
    if ticket_type == 'купе':
        place = input('Выберите одно из свободных мест: 5, 13, 8: ')
    elif ticket_type == 'плацкарт':
        print('В плацкате мест не осталось, ждите следующий')
        exit()
elif transport == 'автобус':
    ticket_type = input('Как вы хотите ехать: сидя, стоя: ')
    if ticket_type == 'сидя':
        place = input('Выберите место: 1, 13, 43: ')
    else:
        place = 'Где угодно'
else:
    print('Такого вида транспорта нет')
    exit()

print('Ок, внесите оплату')
print('Вы выбрали: ', transport,',','ваше место: ', place)

'''

food_choise = input('ЧТо закажете: шаурма, самса, пирожок: ')
if food_choise == 'шаурма':
    filling = input('Какую начинку вы хотиите: мясо, курица: ')
elif food_choise == 'самса':
    filling = input('Какую начинку вы хотите: мясо, курица, сыр: ')
    if filling == 'сыр':
        choise = input('Самсы с сыром закончились, вы будете ждать: да, нет: ')
        if choise == 'нет':
            exit()
elif food_choise == 'пирожок':
    filling = input('Какую начинку вы хотите: картошка, капуста: ')
else:
    print('Такого блюда нет')
    exit()

how_much = input('Сколько закажете: ')
warm = input('Разогреть: да, нет: ')
drink = input('Что будете пить: чай, кофе, кола, минералка: ')
if drink == '':
    print('Вы заказали', food_choise, filling, how_much, ',', 'клиент напиток не взял')
else:
    print('Вы заказали', food_choise, 'c', filling, how_much, 'шт', ',', drink)

