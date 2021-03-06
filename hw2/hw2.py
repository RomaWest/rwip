# Задание 1
# (Подсказка: ищите как это сделать с помощью методов строк)
# 1.	Определите является ли строка записью числа. (Подсказка: ищите как это сделать с помощью методов строк)
S = 'a123'
S.isnumeric()

# 2.	Посчитайте сколько у вас пробелов в строке.
S = 'a 123 '
S.count(' ')

# 3.	Посчитайте сколько у вас символов точки '.' в строке.
S = 'a .123 .'
S.count('.')

# 4.	Создайте строку "Homework". Преобразуйте ее в строку длиной 100 символов, посередине которой исходное слово,
#  а с обоих сторон строка заполнена пробелами. Выведите ее на экран.
S = 'Homework'
S.replace('Homework', ' '*46 + 'Homework' + ' '*46)

# 5.	Сделайте первые буквы слов строки большими (upper case).
S = 'upper case'
S.title()

# Задание 2
# 1.	Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 179 и 971.
import math
c = math.sqrt(179**2 + 971**2)
print(c)

# 2.	Дано двузначное число. Найдите число десятков в нем.
print('48'[0])

# 3.	Дано трехзначное число. Найдите сумму его цифр.
c = '516'
print(int(c[0])+int(c[1])+int(c[2]))

# 4.	Дано целое число n. Выведите следующее за ним чётное число.
n = 2
n += 1
while n % 2 != 0:
    n += 1
print(n)

# 5.	Дано положительное действительное число X. Выведите его дробную часть.
print(str(3.456).split('.')[1])

# 6.	Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
print(str(3.456).split('.')[1][0])

# Задание 3
# Пользователь вводит целое число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским
# календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

n = int(input('Введите целое число: '))

if n % (4 or 400) == 0 and n % 100 !=0:
    print('YES')
else:
    print('NO')

# Задание 4
# Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами. Если треугольник существует,
# выведите строку YES, иначе выведите строку NO.
i = 0
lst = ['a', 'b', 'c']

while i < 3:
    lst[i] = float(input('Введите число для стороны ' + lst[i] + ': '))
    i += 1

print(lst)
if 0 < float(lst[0]) and 0 < float(lst[1]) and 0 < float(lst[2]):
    print('YES')
else:
    print('NO')

# Задание 5
# Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три числа a, b, c, затем программа
# должна менять их значения так, чтобы стали выполнены условия a <= b <= c, затем программа выводит тройку a, b, c.
# Дополнительные ограничения: нельзя использовать дополнительные переменные.
i = 0
lst = ['a', 'b', 'c']

while i < 3:
    lst[i] = float(input('Введите число ' + lst[i] + ': '))
    i += 1

lst.sort()
print(lst)

# Задание 6
# Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
i = 0
lst = ['a', 'b', 'c']

while i < 3:
    lst[i] = int(input('Введите число ' + lst[i] + ': '))
    i += 1

print(lst)
if int(lst[0]) == int(lst[1]) == int(lst[2]):
    print(3)
elif (int(lst[0]) in (int(lst[1]), int(lst[2]))) or (int(lst[2]) in (int(lst[0]), int(lst[1]))):
    print(2)
else:
    print(0)
