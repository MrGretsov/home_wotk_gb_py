# Найдите сумму цифр трехзначного числа.
try:
    number = int(input("Введите трехзначное число: "))
    if number > 100 and number < 1000:
        sum = 0
        while ( number != 0):
            sum = sum + number%10
            number = number // 10
        print('Cумма цифр введеного Вами числа составляет:'+ str(sum))
    else:
        print("Пожалуйста введите трехзначное число")
except:
    print('Вы ввели некорректные данные')