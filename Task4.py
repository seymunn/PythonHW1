# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали
# одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

shadoof_all = int(input("Введите кол-во журавликов: "))

if shadoof_all % 6 == 0:
    shadoof_boys = shadoof_all // 6
    shadoof_girl = shadoof_boys * 4
    print(f"Катя сделала {shadoof_girl} журавликов, а Петя и Сережа по {shadoof_boys} журавликов")
else:
    print("Нет решения")