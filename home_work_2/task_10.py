# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
from random import randint
n = int(input('Введите количество монеток '))
lst = [randint(0, 1) for i in range(n)] # 0 это решка , 1 это орёл
print(f'{n} -> {lst}')
count_one = 0
count_two = 0
for i in lst:
    if i == 0:
        count_one += 1
    elif i == 1:
        count_two += 1
if count_one > count_two and count_one != n:
    print(f'необходимо перевернуть {count_two} ')
elif count_two > count_one and count_two != n:
    print(f'необходимо перевернуть {count_one} ')
elif count_one == count_two:
    print(f'Выбор за тобой,какую хочешь такую и переворачивай')
elif count_one == n or count_two == n:
    print(f'Ничего не трогай,всё и так отлично')