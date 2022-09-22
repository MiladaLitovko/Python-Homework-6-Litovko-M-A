# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Оригинальное решение

import math

def difference():
    list = [1.1, 1.2, 3.1, 5, 10.01]
    for i in range(len(list)):
        list[i] = list[i] % 1
    maximum = max(list)
    minimum = min(list)
    dif = maximum - minimum
    dif = str(dif)
    return(dif[0:4]) 

print(difference())

# Новое решение
import math

org_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = list(map(lambda x: x % 1, org_list))
dif = str(max(new_list) - min(new_list))

print(dif[0:4])
