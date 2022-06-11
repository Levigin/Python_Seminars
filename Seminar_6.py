from collections import deque


LIST_OPERATION = ['+', '-', '*', '/', '(', ')']


def main(math_expression: str):
    expression_list = get_expression(math_expression)
    return calc(expression_list)


def get_expression(expression: str):
    expr_list = []
    item = 0
    while item < len(expression):

        if expression[item] == " ":
            item += 1
            continue

        if expression[item] in LIST_OPERATION:
            expr_list.append(expression[item])
            item += 1
        else:
            start_index = item
            while expression[item] not in LIST_OPERATION:
                if item == len(expression) - 1:
                    item += 1
                    break
                else:
                    item += 1
            expr_list.append(expression[start_index: item])

    return expr_list


def get_expr_in_parenthesis(expr_list: list):
    d = deque()
    parenthesis_dict = {}

    for parenthesis in range(len(expr_list)):
        if expr_list[parenthesis] == '(':
            parenthesis_dict[parenthesis] = parenthesis
            d.append(parenthesis)
        elif expr_list[parenthesis] == ')':
            parenthesis_dict[d.pop()] = parenthesis
    print(parenthesis_dict)
    return parenthesis_dict


def calc_mul_div(expr_list: list):

    expr_list_without_muldiv = []
    i = 0
    while i < len(expr_list):
        if expr_list[i] == "*":
            expr_list_without_muldiv[len(expr_list_without_muldiv) - 1] = float(expr_list_without_muldiv[len(expr_list_without_muldiv) - 1]) * float(expr_list[i + 1])
            i += 1
        elif expr_list[i] == "/":
            expr_list_without_muldiv[len(expr_list_without_muldiv) - 1] = float(expr_list_without_muldiv[len(expr_list_without_muldiv) - 1]) / float(expr_list[i + 1])
            i += 1
        else:
            if isinstance(expr_list[i], float):
                expr_list_without_muldiv.append(float(expr_list[i]))
            else:
                expr_list_without_muldiv.append(expr_list[i])
        i += 1

    return expr_list_without_muldiv


def calc_add_sub(expr_list: list):

    expr_list_without_addsub = []
    i = 0

    while i < len(expr_list):
        if expr_list[i] == "+":
            expr_list_without_addsub[len(expr_list_without_addsub) - 1] = float(
                expr_list_without_addsub[len(expr_list_without_addsub) - 1]) + float(expr_list[i + 1])
            i += 1
        elif expr_list[i] == "-":
            expr_list_without_addsub[len(expr_list_without_addsub) - 1] = float(
                expr_list_without_addsub[len(expr_list_without_addsub) - 1]) - float(expr_list[i + 1])
            i += 1
        else:
            if isinstance(expr_list[i], float):
                expr_list_without_addsub.append(float(expr_list[i]))
            else:
                expr_list_without_addsub.append(expr_list[i])
        i += 1

    return expr_list_without_addsub[0]


def calc(expr_list: list):

    result = 0

    parenthesis_dict = get_expr_in_parenthesis(expr_list)
    open_parenthesis = list(parenthesis_dict.keys())
    close_parenthesis = list(parenthesis_dict.values())

    if len(parenthesis_dict) != 0:
        # print(len(parenthesis_dict))
        i = len(parenthesis_dict) - 1

        while i >= 0:
            temp_list = calc_add_sub(calc_mul_div(expr_list[open_parenthesis[i] + 1: close_parenthesis[i]]))
            del expr_list[open_parenthesis[i] + 1: close_parenthesis[i] + 1]
            expr_list[open_parenthesis[i]] = calc_add_sub(temp_list)
            i -= 1

        new_list_expr = calc_mul_div(expr_list)
        result = calc_add_sub(new_list_expr)

    else:
        new_list_expr = calc_mul_div(expr_list)
        result = calc_add_sub(new_list_expr)

    return result


# print(main('1-2*2/2*2-2/2*2+1'))
# print(main('2+2/2'))
# print(main('(2+6) / (3+1)'))
print(main('(((10+2)+2)+1)'))


# 2.
#
#
# def rle():
#     result = ''
#     symbol = ''
#     counter = 1
#     with open('text_for_task2-in_seminar6.txt', 'r', encoding='UTF-8') as file:
#         text = file.read()
#         for curr_symbol in text:
#             if curr_symbol != symbol:
#                 if symbol:
#                     result += str(counter) + symbol
#                 counter = 1
#                 symbol = curr_symbol
#             else:
#                 counter += 1
#         else:
#             result += str(counter) + symbol
#
#     file.close()
#
#     with open('text_for_task2-in_seminar6_compressed.txt', 'w', encoding='UTF-8') as file:
#         file.write(result)
#
#     file.close()
#
#
# rle()

# 3


# def rot_13(text: str) -> str:
#     new_text = ''
#     for i in text:
#         new_text += str(chr(ord(i)+13))
#
#     return new_text
#
#
# def decode(text: str):
#     new_text = ''
#     for i in text:
#         new_text += str(chr(ord(i) - 13))
#
#     return new_text
#
#
# string = 'abc bca'
# new_string = rot_13(string)
# print(new_string)
# print(decode(new_string))


