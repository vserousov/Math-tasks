# coding=utf-8
__author__ = 'Сероусов Виталий'
import math

class Point(object):
    """
    Класс точка
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape(object):
    """
    Класс фигура
    """
    def square(self):
        pass
    def perimeter(self):
        pass
    @property
    def is_even(self):
        pass


class Triangle(Shape):
    """
    Класс треугольник
    """
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)
        self.c = Point(x3, y3)
        self.AB = math.sqrt((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2)
        self.BC = math.sqrt((self.c.x - self.b.x) ** 2 + (self.c.y - self.b.y) ** 2)
        self.AC = math.sqrt((self.c.x - self.a.x) ** 2 + (self.c.y - self.a.y) ** 2)

    def perimeter(self):
        return self.AB + self.BC + self.AC

    def square(self):
        p = self.perimeter() / 2
        return p * (p-self.AB)*(p-self.BC)*(p-self.AC)

    @property
    def is_even(self):
        return self.AB == self.BC and self.BC == self.AC


class Rectangle(Shape):
    """
    Класс прямоугольник
    """
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)
        self.c = Point(x3, y3)
        self.d = Point(x4, y4)
        self.AB = math.sqrt((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2)
        self.BC = math.sqrt((self.c.x - self.b.x) ** 2 + (self.c.y - self.b.y) ** 2)
        self.CD = math.sqrt((self.d.x - self.c.x) ** 2 + (self.d.y - self.c.y) ** 2)
        self.AD = math.sqrt((self.d.x - self.a.x) ** 2 + (self.d.y - self.a.y) ** 2)

    def perimeter(self):
        return self.AB + self.BC + self.CD + self.AD

    def square(self):
        return self.AB * self.BC;

    @property
    def is_even(self):
        return self.AB == self.BC