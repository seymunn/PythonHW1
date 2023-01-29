# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket_number = int(input("Введите номер билета: "))
sum_first_part = 0
sum_second_part = 0

sum_first_part += ticket_number // 100000
sum_first_part += ticket_number // 10000 % 10
sum_first_part += ticket_number // 1000 % 10

sum_second_part += ticket_number % 10
sum_second_part += ticket_number // 10 % 10
sum_second_part += ticket_number // 100 % 10

if sum_first_part == sum_second_part:
    print(f"Билет с номером {ticket_number} счастливый")
else:
    print(f"Билет с номером {ticket_number} не счастливый")