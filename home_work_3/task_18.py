# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
N = int(input('Введите число: '))
spisok = list(range(1,N+1))
print(spisok)
X = int(input('Введите число Х: '))
for i in spisok:
    if i == X - 1 or i == X + 1:
        print('Близкий по величине элемент к заданному числу', X , '\nявляется число',i)