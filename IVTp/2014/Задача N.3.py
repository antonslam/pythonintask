﻿# Задача N.3.13 Вариант V.13
# Напишите программу, которая выводит имя "Норма Бейкер", и запрашивает его псевдоним. 
# Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.
print ('Задача N.1.13 Вариант V.13 \nНапишите программу, которая выводит имя "Норма Бейкер", и запрашивает его псевдоним.  \nПрограмма должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире. \n\n\n\n\n')


name = "Норма Бейкер"
alias = "мэрилин"
print("Вопрос про человека по имени" + name)
aliass = input("Под каким же именем мы знаем этого человека? Ваш ответ: ")
if (aliass == alias):
	print("На вопрос Вы ответили верно!")
else:
	print("На вопрос Вы ответили неверно!")


input ("Выход?")