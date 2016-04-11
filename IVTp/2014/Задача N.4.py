# Задача N.4.13 Вариант V.13 Кезич
# Напишите программу, которая бы при запуске случайным образом
# отображала имя одного из двенадцати апостолов.
print ('Задача N.4.13 Вариант V.13 \nНапишите программу, которая бы при запуске случайным образом  \nотображала имя одного из двенадцати апостолов. \n\n\n\n\n')


import random

names = random.randint(1,12)


if names == 1 :
    print('Андрей')
elif names == 2 :
    print('Пётр') 
elif names == 3 :
    print('Иоанн') 
elif names == 4 :
    print('Иаков Зеведеев ') 
elif names == 5 :
    print('Филипп из Вифсаиды') 
elif names == 6 :
    print('Варфоломей') 
elif names == 7 :
    print('Матфей') 
elif names == 8 :
    print('Фома') 
elif names == 9 :
    print('Симон Кананит')
elif names == 10 :
    print('Иаков Алфеев') 	
else :
    print('Иуда (Искариот)')



input ("Выход?")