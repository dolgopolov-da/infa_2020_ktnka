'''
Разбиение на чанки 🌶️

На вход программе подаются две строки, на одной символы, на другой число
n. Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число,
задающее размер чанка (куска), а возвращает список из чанков указанной длины.
'''

txt = input().split()
n = int(input())

def chunked(list, len_chunk):
    lst = []
    sublst = []
    for i in range(len(txt)):
        sublst.append(txt[i])
        if i == len(txt) - 1:
            lst.append(sublst)
        elif len(sublst) < n:
            continue
        else:
            lst.append(sublst)
            sublst = []
    return lst

char_list = chunked(txt, n)
print(char_list)
