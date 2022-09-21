'''
Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
# Оригинальное решение
def odd_numbers():
    list = [1, 3, 6, 1, 46, 5, 32, 7]
    sum = 0
    for index in range(len(list)):
        if index % 2 != 0:
            sum = sum + list[index]
    return sum

print(odd_numbers())

# Новое решение
list = [1, 3, 6, 1, 46, 5, 32, 7]
summa = sum(list[index] for index in range(len(list)) if index % 2 != 0)
print(summa)
