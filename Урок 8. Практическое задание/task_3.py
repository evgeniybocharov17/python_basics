"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

#Создание собственного класса исключения
class IsNotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

#исходные данные
list_of_numbers = []
number = 0
print(f"Данная программа запрашивает числа и объединяет их в список.\n"
      f"Для завершения программы введите слово stop\n")

#Цикл: Запрос чисел, объеденение чисел в список, вывод списка чисел на экран.
#Если введено вместо числа другие символы, на экран выводится оповещение об этом
#и вновь запрашивается число.
#Цикл продолжается, до тех пор пока не будет введено "stop".

while number != "stop":
    try:
        number = input("Введите число:")
        if number == "stop":
            break
        elif number.isdigit() == True:
            list_of_numbers.append(int(number))
        else:
            raise IsNotNumber("Вы ввели не число")

    except IsNotNumber as err:
        print(err)


print(f"результат: {list_of_numbers}")
print("Программа завершена")






