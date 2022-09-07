'''Шифр Цезаря'''

import random

def lang_selection(dict1_lower, dict1_upper, dict2_lower, dict2_upper):
    # выбор языка шифруемого сообщения
    while True:
        lang_selection = input('Укажите язык шифруемого сообщения: "ru"/"1" или "en"/"2": ')
        if lang_selection == 'ru' or lang_selection == '1':
            return dict1_lower, dict1_upper
        elif lang_selection == 'en' or lang_selection == '2':
            return dict2_lower, dict2_upper
        else:
            print('Неверный ввод')


def encrypt_text(text, dict_low, dict_up=[], digits=[], punctuation=[]):
    rot_n = random.randrange(1, len(dict_low))
    print(f'Используемое преобразование в шифре Цезаря: ROT_{rot_n}')
    encrypted_dict_low = ''
    encrypted_dict_up = ''
    encrypted_text = ''

    for i in range(len(dict_low)):
        encrypted_dict_low += dict_low[(i + rot_n) % len(dict_low)]
    for i in range(len(dict_up)):
        encrypted_dict_up += dict_up[(i + rot_n) % len(dict_up)]

    for i in range(len(text)):
        if text[i] in dict_low:
            encrypted_text += encrypted_dict_low[dict_low.find(text[i])]
        elif text[i] in dict_up:
            encrypted_text += encrypted_dict_up[dict_up.find(text[i])]
        elif text[i] in digits:
            encrypted_text += text[i]
        elif text[i] in punctuation:
            encrypted_text += text[i]

    return encrypted_text


def main():
    # строка латинских символов
    en_dict_lower = 'abcdefghijklmnopqrstuvwxyz'
    en_dict_upper = ''.join([en_dict_lower[i].upper() for i in range(len(en_dict_lower))])

    # строка кириллических символов
    ru_dict_lower = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    ru_dict_upper = ''.join([ru_dict_lower[i].upper() for i in range(len(ru_dict_lower))])

    # строки нешифруемых символов
    digits = '0123456789'
    punctuation = ',.;:!#$%&*+-=?@^_ '

    # выбор языка шифруемого сообщения
    dict_lower, dict_upper = lang_selection(ru_dict_lower, ru_dict_upper, en_dict_lower, en_dict_upper)

    # ввод и проверка шифруемого сообщения
    is_message_valid = False
    while not is_message_valid:
        message = input('Введите шифруемое сообщение: ')
        for i in range(len(message)):
            if message[i] not in dict_lower + dict_upper + digits + punctuation:
                print('В шифруемом сообщении обнаружен символ из другого языка.')

                while True:
                    print('Выберите действие:', '1 - ввести сообщение', '2 - изменить выбор языка', sep='\n')
                    reselect = input()
                    if reselect == '1':
                        break
                    elif reselect == '2':
                        dict_lower, dict_upper = lang_selection(ru_dict_lower, ru_dict_upper,
                                                                en_dict_lower, en_dict_upper)
                        break
                    else:
                        print('Неверный ввод')
                break
            else:
                is_message_valid = True

    # шифрование сообщения
    encrypted_message = encrypt_text(message, dict_lower, dict_upper, digits, punctuation)

    print(f'Незашифрованное сообщение: "{message}"')
    print(f'Зашифрованное сообщение: "{encrypted_message}"')


main()