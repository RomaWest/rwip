s = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to bе
(Football Coach)"""

"""•	Посчитайте сколько слов в тексте (разбейте на слова методом строк split)"""
s1 = s.split('\n')
s2 = []
for i in s1:
    s2.extend(i.split(' '))
print(len(s2))

"""•	Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)"""
s3 = []
for i in s2:
    s3.append(i.strip('.!()'))
print(s3)

"""•	Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)"""
s3.sort()
print(s3)

"""•	Посчитать, сколько раз встречается каждое слово.
(Подсказка: создавать словарь, где ключи — это слова из текста,
 а в значениях подсчитываем количество «встречаний» этого слова)"""
import operator

dct = {}

for i in s3:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

sorted_dct = sorted(dct.items(), key=operator.itemgetter(1), reverse=True)
d = dict((x, y) for x, y in sorted_dct)

for i in d:
    print(i, d[i])
