""" Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
 а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10 """

totalNumber = int(input('Какое количество журавликов сделали дети: '))
katya = int(totalNumber / 3 * 2) 
petya = int(katya / 2 / 2)
serega = int(petya)
print(katya, petya, serega)
