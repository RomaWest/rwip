""" 1.	Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым"""

lst = list(range(10))
while len(lst) > 0:
    print(lst.pop(0))
print('Control: ', lst, end='\n'*2)


""" 2.	** Как сделать это же задание со строкой?"""

s = '0123456789'
while len(s) > 0:
    print(s[0])
    s = s[1:]
print('Control: ', s, end='\n'*2)


""" 3.	Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого, 
пока он не останется пустым."""

lst = list('xyzabc')
while len(lst) > 0:
    lst.sort()
    print(lst.pop(0))
print('Control: ', lst, end='\n'*2)
