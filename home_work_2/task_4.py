#  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input('Введите число '))
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(k))
new_list = []
for item in data:
    new_list.append(-item)

last_spisok = new_list + data
last_spisok.append(0)
last_spisok.sort()
print(last_spisok)