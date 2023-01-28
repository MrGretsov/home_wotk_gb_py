# HARD необязательная, идет за 3 обязательных
# Найдите сумму цифр любого вещественного или целого числа.
# Можно использовать decimal. Через строку решать нельзя.
try:
    number = float(input('Введите число '))
    if number == int(number) :
        sum = 0
        while (number != 0):
            sum = int(sum) + number % 10
            number = number // 10
        print('Cумма цифр введеного Вами числа составляет:' + str(sum))
    else:
        count = len(list(str(number)))-1
        new_number = round(number%1,count)
        # print(new_number)
        number_2 = len(list(str(new_number)))-2
        # print(number_2)
        number_3 = number*10**number_2
        # print(number_3)
        sum = 0
        while (number_3 != 0):
            sum = int(sum) + number_3 % 10
            number_3 = number_3 // 10
        print('Cумма цифр введеного Вами числа составляет:' + str(sum))

except:
    print('Вы ввели некорректные данные')