"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

#Создание собственного класса исключения
class MyZeroDivisionError(Exception):
   def __init__(self, txt):
       self.txt = txt

#запрос данных от пользователя
divid = input("Введите делимое:")
divider = input("Введите делитель:")


try:
    #переводим введенные данные из типа str в тип int
    divid = int(divid)
    divider = int(divider)

    #условие при котором поднимается исключение MyZeroDivisionError
    if divider == 0:
        raise MyZeroDivisionError("На ноль делить нельзя!")

#Обработка ситуации, когда происходит деление на 0 (по правилам на 0 делить нельзя)
except MyZeroDivisionError as err:
    print(err)

#обработка корректной ситуации, когда в качестве делителя введено любое число кроме нуля.
else:
    res = divid / divider
    print(f"Результат: {res}")


