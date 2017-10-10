"""Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
 и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний),
 Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle)."""


def triangle(a, b, c):

    if 0 < a and 0 < b and 0 < c:
        if a == b == c:
            return 'Equilateral triangle'
        elif a == b or a == c or b == c:
            return 'Isosceles triangle'
        else:
            return 'Versatile triangle'
    else:
        return False


print(triangle(int(input()), int(input()), int(input())))