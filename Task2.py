'''
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
# Оригинальное решение

def pairs():
    list = [2, 3, 4, 5, 6]
    newlist = []
    b = -1
    if len(list) % 2 == 0:
        for i in range(len(list) // 2):
            a = list[i] * list[b]
            b -= 1
            newlist.append(a)
    else:
        for i in range((len(list) - 1) // 2 + 1):
            if i != ((len(list) - 1) // 2):
                a = list[i] * list[b]
                b -= 1
                newlist.append(a)
            else:
                a = list[i] * list[i]
                newlist.append(a)
    return(newlist)

print(pairs())




# Новое решение
def pairs():
    list = [2, 3, 4, 5, 6]
    newlist = []
    b = -1
    
    if len(list) % 2 == 0:
            newlist = [a for i in range(len(list) // 2)  ]
        for i in range(len(list) // 2):
            a = list[i] * list[b]
            b -= 1
            newlist.append(a)
    else:
        for i in range((len(list) - 1) // 2 + 1):
            if i != ((len(list) - 1) // 2):
                a = list[i] * list[b]
                b -= 1
                newlist.append(a)
            else:
                a = list[i] * list[i]
                newlist.append(a)
    return(newlist)

print(pairs())