import random

guess_number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(text):
    for i in range(len(text)):
        if not text[i].isdigit():
            return False
    if not int(text) in range(1, 101):
        return False
    else:
        return True

def main():
    game = True
    while game:
        txt = input('Введите число от 1 до 100: ')
        if not is_valid(txt):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            user_number = int(txt)

        if user_number < guess_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_number > guess_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            game = False
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

main()