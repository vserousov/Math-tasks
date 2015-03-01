# coding=utf-8
__author__ = 'Сероусов Виталий'

from shape import Point
import math

class Vector(object):
    """
    Класс вектора
    """
    def __init__(self, x1, y1, x2, y2):
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)
        self.coord = Point(x2 - x1, y2 - y1)

    def __add__(self, vector):
        return Vector(self.start.x + vector.start.x,
                      self.start.y + vector.start.y,
                      self.end.x + vector.end.x,
                      self.end.y + vector.end.y)

    def __lt__(self, vector):
        first = math.sqrt(self.coord.x ** 2 + self.coord.y ** 2)
        second = math.sqrt(vector.coord.x ** 2 + vector.coord.y ** 2)
        return first == second

    def __sub__(self, vector):
        return Vector(self.start.x - vector.start.x,
                      self.start.y - vector.start.y,
                      self.end.x - vector.end.x,
                      self.end.y - vector.end.y)

    def angle(self, vector):
        scalar = self.coord.x * vector.coord.x + self.coord.y * vector.coord.y
        firstLength = math.sqrt(self.coord.x ** 2 + self.coord.y ** 2)
        secondLength = math.sqrt(vector.coord.x ** 2 + vector.coord.y ** 2)
        return math.acos(abs(scalar) / (firstLength * secondLength)) * (180/math.pi)

