# coding=utf-8
__author__ = 'Сероусов Виталий'


class TypeException(BaseException):
    """
    Исключение при неправильном типе
    """
    def __init__(self, allowed_type):
        self.message = "Ошибка типа! Разрешено только: " + allowed_type


class RangeException(BaseException):
    """
    Исключение при выходе за диапазон
    """
    def __init__(self, message):
        self.message = "Ошибка диапазона! " + message


class ZeroException(BaseException):
    """
    Исключение при делении на ноль
    """
    def __init(self):
        self.message = "Деление на ноль!"

def try_parse(message):
    """
    Рекурсивный метод парсинга int и float
    :param message: Текст на экране
    :return: Значение int/float
    """
    argument = raw_input(message)
    try:
        if '.' in argument:
            return float(argument)
        else:
            return int(argument)
    except:
        return try_parse(message)