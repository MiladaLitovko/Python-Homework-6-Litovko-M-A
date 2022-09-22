'''
Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
Пример
-Для "abababb" и "aba" -> 2
'''
'''
# Оригинальное решение

str1 = str(input('Введите строку 1: '))
str2 = str(input('Введите строку 2: '))
count = 0


for i in range(0,len(str1)):
    if str1[i] == str2[0]:
        if str2 == str1[i: i + len(str2)]:
            count += 1
            i += len(str2)
print(count)
'''

# Новое решение
str1 = str(input('Введите строку 1: '))
str2 = str(input('Введите строку 2: '))
count = 0

out = sum(count + 1 for i in range(0,len(str1)) if str1[i] == str2[0] and str2 == str1[i: i + len(str2)])

print(out)