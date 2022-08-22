'''Делители-1 🌶️

На вход программе подается два натуральных числа
a и b (a < b). Напишите программу, которая находит натуральное число из отрезка
[a;b] с максимальной суммой делителей.
'''

a = 1
b = 1000
max_num = a
max_count = 0
max_total = 0

for i in range(a, b + 1):
    count = 0
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            total += j
    if total >= max_total:
        max_count = count
        max_num = i
        max_total = total

print(max_num, max_total)
