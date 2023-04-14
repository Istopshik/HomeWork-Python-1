'''
Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''
print("Введите трехзначное число: ")
numbers = input()
result = 0
if int(numbers) > 99 and int(numbers) < 1000:
    for i in numbers:
        result += int(i)
    print(result)
else:
    print("Вы ввели не трехзначное число!")    


            
    
    