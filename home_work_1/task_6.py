# Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
try:
    ticket = int(input('Введите номер билета '))
    if ticket >= 100000 and ticket <= 999999:
        number_ticket_one = int(ticket/1000)
        number_ticket_two = int(ticket%1000)
        sum_one = 0
        while (number_ticket_one != 0):
            sum_one = int(sum_one) + number_ticket_one%10
            number_ticket_one = number_ticket_one/10
        sum_two = 0
        while(number_ticket_two != 0):
            sum_two = int(sum_two) + number_ticket_two%10
            number_ticket_two = number_ticket_two/10
        if sum_one == sum_two:
            print('Билет счастливый!')
        else:
            print('Билет не счастливый :(')
    else:
        print('Номер билета должен быть шестизначным')
except:
    print('Вы ввели некорректные данные')