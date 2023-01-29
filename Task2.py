# Найдите сумму цифр трехзначного числа.
# Пример:
# 100 -> 1 (1 + 0 + 0)
# 123 -> 6 (1 + 2 + 3)

number = int(input("Введите число: "))
numsum = 0

if number > 99 and number < 1000:
    while number > 0:
        numsum += number % 10
        number //= 10
    print(f"{number} -> {numsum}")
else:
    print("Указанное число выходит за пределы допустимого значения")