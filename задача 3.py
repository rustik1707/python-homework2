'''Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8'''
N = int(input('введите число: '))

m = 1
while m <= N:
    print (m,end=' ')
    m = m * 2

