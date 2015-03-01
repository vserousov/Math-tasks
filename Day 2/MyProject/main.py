# coding=utf-8
from serousov.tasks import *

print "Список задач:"
for i in xrange(1, 17):
    print str(i) + " - Task" + str(i)
print "Для выхода из программы введите 0"

while True:
    number = try_parse("Введите номер задачи: ")

    if number == 0:
        break
    elif number == 1:
        task1()
    elif number == 2:
        a = try_parse("Введите исходное число: ")
        task2(a)
    elif number == 3:
        a = try_parse("Введите исходное число: ")
        task3(a)
    elif number == 4:
        a = try_parse("Введите аргумент факториала: ")
        print task4(a)
    elif number == 5:
        a = try_parse("Введите аргумент функции: ")
        print task5(a)
    elif number == 6:
        a = try_parse("Введите аргумент функции: ")
        print task6(a)
    elif number == 7:
        a = try_parse("Число, из которого извлекается корень: ")
        print task7(a)
    elif number == 8:
        print task8()
    elif number == 9:
        task9()
    elif number == 10:
        n = try_parse("Введите число n:")
        k = try_parse("Введите число k:")
        task10(n, k)
    elif number == 11:
        k = try_parse("Введите число k:")
        print task11(k)
    elif number == 12:
        N = try_parse("Введите число элементов массива:")
        task12(N)
    elif number == 13:
        n = try_parse("Введите число элементов массива:")
        if n < 2:
            raise RangeException("Число элементов массива не может быть меньше 2")
        arr = [randint(1, 100) for i in xrange(n)]
        print task13(arr)
    elif number == 14:
        n = try_parse("Введите размерность матрицы: ")
        print task14(n)
    elif number == 15:
        print task15()
    elif number == 16:
        a = try_parse("Введите число а: ")
        b = try_parse("Введите число b: ")
        print task16(a, b)
    else:
        print "Ошибка! Задачи с таким номером не существует."