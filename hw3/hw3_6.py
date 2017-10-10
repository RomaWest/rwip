""" 1)	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный,
 и False иначе."""


def is_year_leap(year):
    if year % (4 or 400) == 0 and year % 100 != 0:
        return True
    else:
        return False


print(is_year_leap(int(input())))


""" 2)	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
Если треугольник существует, вернёт True, иначе False."""


def triangle(a, b, c):
    if 0 < a and 0 < b and 0 < c:
        return True
    else:
        return False


print(triangle(int(input()), int(input()), int(input())))
