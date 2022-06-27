# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо.
# Используйте знания с последней лекции. Выполните ее в виде функции


# def del_char(text: list):
#     return list(filter(lambda x: x.find('да') == -1, text))
#
#
# print(del_char(['дааддавлвда', 'лллфффаб']))

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"?
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

def tic_tac_toe():

    tic_tac_toe_field = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    flag = True
    while True:
        try:
            x, y = map(int, input("Enter the coordinate separated by space: ").split())
            if 0 <= x < 3 and 0 <= y < 3:
                if flag:
                    if tic_tac_toe_field[x][y] not in tic_tac_toe_field and tic_tac_toe_field[x][y] != '0':
                        tic_tac_toe_field[x][y] = 'x'
                        print_tic_tac_toe_field(tic_tac_toe_field)
                        flag = False
                    else:
                        print("You can't put it here")

                else:
                    if tic_tac_toe_field[x][y] not in tic_tac_toe_field and tic_tac_toe_field[x][y] != 'x':
                        tic_tac_toe_field[x][y] = '0'
                        print_tic_tac_toe_field(tic_tac_toe_field)
                        flag = True
                    else:
                        print("You can't put it here")
            else:
                print('This coordinate is not exist!')

            if check_the_field(tic_tac_toe_field):
                print('\nYou win!')
                break
            else:
                continue
        except Exception as e:
            print("Invalid input!", e)


def print_tic_tac_toe_field(tic_tac_toe_field):
    for i in range(len(tic_tac_toe_field)):
        for j in range(len(tic_tac_toe_field[0])):
            print(f'|{tic_tac_toe_field[i][j]}|', end=" ")
        print()


def check_the_field(tic_tac_toe_field):
    res_row = []
    res_col = []
    res_diagonal = []
    res_diagonal1 = []

    l = len(tic_tac_toe_field)

    for i in range(len(tic_tac_toe_field)):
        temp = []
        for j in range(len(tic_tac_toe_field)):
            temp.append(tic_tac_toe_field[j][i])
        res_col.append(temp)
        res_row.append(tic_tac_toe_field[i])
        res_diagonal.append(tic_tac_toe_field[i][i])
        res_diagonal1.append(tic_tac_toe_field[l - i - 1][i])

    res_diagonal = all(x == res_diagonal[0] for x in res_diagonal) and all(x != " " for x in res_diagonal)
    res_diagonal1 = all(x == res_diagonal1[0] for x in res_diagonal1) and all(x != " " for x in res_diagonal1)

    if res_diagonal or res_diagonal1:
        return True

    for i in res_row:
        if all(x == i[0] for x in i) and all(x != " " for x in i):
            return True
    for i in res_col:
        if all(x == i[0] for x in i) and all(x != " " for x in i):
            return True

    return False


tic_tac_toe()


# 3

# def filter():
#     crutches = ['короче говоря', 'короче', 'кстати', 'эээээ', 'эээ', 'ээээ', 'кажется', 'ясен пень', 'в общем', 'ну', 'как бы']
#     with open("Text_3.txt", "r", encoding='utf-8') as file:
#         test_file = file.read().lower()
#         for item in crutches:
#             test_file = test_file.replace(', ' + item, '')
#         for item in crutches:
#             test_file = test_file.replace(' , ' + item, '')
#         for item in crutches:
#             test_file = test_file.replace(item, '')
#     while test_file[1] == ',' or test_file[1] == ' ' or test_file[1] == '...':
#         test_file = test_file[1:]
#
#     test_file = '«' + test_file
#
#     with open("Text_3.txt", "w", encoding='utf-8') as file:
#         file.write(test_file)
#
#
# filter()


# 4

# from functools import reduce
#
#
# def get_sum():
#     prog_languages = ['Java', 'C', 'C#', 'C++', 'Kotlin', 'Python', 'Ruby', 'Javascript', 'Typescript', 'Swift']
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
#     list_lang = [(i, prog_languages[i - 1].upper()) for i in numbers if i <= len(prog_languages)]
#     new_list = [(reduce(lambda x, y: x + ord(y), i[1], 0), i[1]) for i in list_lang if reduce(lambda x, y: x + ord(y), i[1], 0) % i[0] == 0]
#     return reduce(lambda x, y: x + y[0], new_list, 0)
#
#
# print(get_sum())