# coding=utf-8
__author__ = 'Сероусов Виталий'

import math
from random import randint

def task1():
    """
    Функция, возвращающая числа из диапазона от a до b, содержащие n-ое число семёрок
    """
    a = int(raw_input("Введите начальный диапазон a:"))
    b = int(raw_input("Введите конечный диапазон b:"))
    n = int(raw_input("Введите число встречаемости числа 7:"))
    count = 0
    for x in range(a,b):
        if (str(x).count('7') == n):
            count +=1
            print x
    if count == 0:
        print "Указанных чисел нет в диапазоне"

def task2(n):
    """
    Функция, выводящая на экран число, записанное в обратном порядке
    :param n: Исходное число
    """
    assert type(n) == int, "Не число"
    assert 100 <= n <= 999, "Число не трехзначное"
    a = n % 10
    c = n / 100
    b = n / 10 - c * 10
    print a * 100 + b * 10 + c

def task3(n):
    """
    Функция, определяющая счастливое число или нет
    :param n: Исходное число
    """
    assert type(n) == int, "Не число"
    assert 1000 <= n <= 9999, "Число не четырехзначное"
    a = n % 10
    c = n / 100
    d = n / 1000
    b = n / 10 - c * 10
    c -= d * 10
    res =  a * 1000 + b * 100 + c * 10 + d
    if (res == n):
        print "Счастливое"
    else:
        print "Несчастливое"

def task4(n):
    """
    Функция, вычисляющая факториал
    :param n: Аргумент факториала
    """
    assert type(n) == int, "Не число"
    assert n >= 0, "Нельзя использовать отрицательные числа"
    if n in range(0,1):
        return 1
    return n * task4(n - 1)

def task5(x):
    """
    Вычисление значения кусочной функции
    :param x: Аргумент функции x
    :return: Значение функции Y(x)
    """
    assert type(x) == float or type(x) == int, "Не число"
    if x <= -0.5:
        return 0.5
    elif -0.5 < x < 0:
        return x + 1
    elif 0 < x <= 1:
        return x * x - 1
    else:
        return x - 1

def task6(x):
    """
    Вычисление значения кусочной функции
    :param x: Аргумент функции
    :return: Значение функции
    """
    assert type(x) == float or type(x) == int, "Не число"
    if (x <= 0.5):
        return math.sin(math.pi / 2)
    else:
        return math.sin((x-1)*math.pi/2)

def task7(x):
    """
    Вычисление кубического корня итерационной функцией
    :param x: Число, из которого извлекается корень
    :return: Количество итераций, значение корня, значение приращения
    """
    current = x
    nextval = current + (x - current**3)/(3 * (current**2))
    i = 0
    while (nextval != next and abs(nextval - current) > 10.0 ** -10):
        i += 1
        current = nextval
        nextval = current + (x - current**3)/(3 * (current**2))
    return i, nextval, (x - current**3)/(3 * (current**2))

def task8():
    """
    Сокращение числителя и знаменателя
    :return: Сокращенная дробь (числитель, знаменатель)
    """
    def nod(a, b):
        if b == 0:
            return a
        else:
            return nod(b, a % b)
    a = int(raw_input("Введите числитель:"))
    b = int(raw_input("Введите знаменатель:"))
    r = nod(a,b)
    return a / r, b / r

def task9():
    """
    Функция, вычисляющая все натуральные числа, равные сумме кубов своих цифр
    """
    for x in range(100, 999):
        a = int(str(x)[0])
        b = int(str(x)[1])
        c = int(str(x)[2])
        if (a ** 3 + b ** 3 + c ** 3 == x):
            print x

def task10(n, k):
    """
    Функция, определяющая k-ю справа цифру числа n
    :param n: Число n
    :param k: Число k
    :return: Результат вычисления
    """
    assert type(n) == int and type(k) == int, "Не числа"
    assert len(str(n)) >= k, "k больше, чем длина числа"
    print str(n)[-k]

def task11(k):
    """
    Функция, вычисляющая k-ое число Фибоначчи
    :param k: Число k
    :return: Число Фибоначчи
    """
    prev = 1
    current = 1
    for x in range(2, k):
        result = current + prev
        prev = current
        current = result
    return result

def task12(N):
    """
    Функция вывода кол-ва простых чисел в массиве
    :param N: Кол-во элементов массива
    :return: Кол-во простых чисел в массиве
    """
    assert type(N) == int, "Не число"
    def checksimple(x):
        if x % 2 == 0:
            return False
        for j in xrange(3, int(math.sqrt(x)) + 1, 2):
            if (x % j == 0):
                return False;
        return True;

    arr = [randint(1, 100) for i in xrange(N)]
    count = 0
    print arr
    for i in arr:
        if checksimple(i):
            count = 1
    print count

def task13(a):
    """
    Нахождение двух минимальных элементов массива
    :param a: Массив
    :return: (1-й минимальный элемент, 2-й минимальный элемент)
    """
    assert type(a) == list, "Не массив"
    a.sort()
    return a[0], a[1]

def task14(N):
    """
    Нахождение суммы элементов матрицы на главной и побочной диагонали
    :param N: Размерность матрицы N*N
    :return: (Сумма эл-тов главной диагонали, Сумма эл-тов побочной диагонали)
    """
    assert type(N) == int and N < 20, "Не число или число, превышающее предел"
    a = [[randint(1, 100) for j in xrange(N)] for i in xrange(N)]
    for i in a:
        print i
    sum1 = 0
    sum2 = 0
    for i in xrange(0, N):
        sum1 += a[i][i];
        sum2 += a[i][N-i-1]
    return sum1, sum2

def task15():
    """
    Нахождение наибольшей разности элементов массива
    :return: Наибольшая разность
    """
    a = [randint(-5, 20) for j in xrange(75)]
    max = -6
    min = 22
    for i in a:
        if i > max:
            max = i
        if i < min:
            min = i
    return max - min

def task16(a, b):
    """
    Нахождение наибольшего общего делителя чисел a и b с помощью алгоритма Эвклида
    :param a: Число a
    :param b: Число b
    :return: Наибольший общий делитель
    """
    assert type(a) == int, "Не число"
    assert type(b) == int, "Не число"
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a

#task1()
#task2(492)
#task3(4554)
#print task4(5)
#print task5(-2)
#print task6(-2)
#print task7(125.0)
#print task8()
#task9()
#task10(123456, 2)
#print task11(10)
#task12(10)
#print task13([1,4,5,2])
#print task14(5)
#print task15()
#print task16(10, 120)