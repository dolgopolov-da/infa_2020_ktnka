'''Гипотеза Эйлера о сумме степеней 🌶️🌶️

В 1769 году Леонард Эйлер сформулировал обобщенную
версию Великой теоремы Ферма, предполагая, что по крайней мере n
энных степеней необходимо для получения суммы, которая сама
является энной степенью для n>2. Напишите программу для
опровержения гипотезы Эйлера (продержавшейся до 1967 года),
и найдите четыре положительных целых числа, сумма 5-х степеней которых
равна 5-й степени другого положительного целого числа.

Таким образом, найдите пять натуральных чисел a,b,c,d,e
удовлетворяющих условию: a**5 + b**5 + c**5 + d**5 = e**5
'''
import time
start_time = time.time()

def main():
    lst_a = []
    lst_b = []
    lst_c = []
    lst_d = []
    lst_e = []

    for a in range(1, 151):
        lst_a.append(a**5)
    for b in range(1, 151):
        lst_b.append(b**5)
    for c in range(1, 151):
        lst_c.append(c**5)
    for d in range(1, 151):
        lst_d.append(d**5)
    for e in range(2, 151):
        lst_e.append(e**5)

    flag = False
    for a in lst_a:
        if flag:
            break
        for b in lst_b:
            if flag:
                break
            for c in lst_c:
                if flag:
                    break
                for d in lst_d:
                    if flag:
                        break
                    if a + b + c + d in lst_e:
                        print('a =', round(a**(1/5)), 'b =', round(b**(1/5)), 'c =', round(c**(1/5)),
                              'd =', round(d**(1/5)), 'e =', round((a + b + c + d)**(1/5)))
                        print(round(a**(1/5) + b**(1/5) + c**(1/5) + d**(1/5) + (a + b + c + d)**(1/5)))
                        flag = True

main()
print("--- {} seconds ---".format(time.time() - start_time))