'''Цифровой корень

На вход программе подается натуральное число n.
Напишите программу, которая находит цифровой корень данного числа.
Цифровой корень числа n получается следующим образом:
если сложить все цифры этого числа, затем все цифры найденной суммы
и повторить этот процесс, то в результате будет получено однозначное число (цифра),
которое и называется цифровым корнем данного числа.
'''

n = int(input())
total = 0
subtotal = 0
subsubtotal = 0

while n > 9:
    total = 0

    while n > 0:
        last_num = n % 10
        total += last_num
        n //= 10
    if total // 10 == 0:
        print(total)
        break
    while total != 0:
        last_num = total % 10
        subtotal += last_num
        total //= 10
    if subtotal // 10 == 0:
        print(subtotal)
        break
    while subtotal != 0:
        last_num = subtotal % 10
        subsubtotal += last_num
        subtotal //= 10
    print(subsubtotal)



