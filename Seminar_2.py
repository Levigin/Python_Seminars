# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
# def sum_odd(vs: list):
#     sum_value = 0
#     for i in range(0, len(vs)):
#         if i % 2 != 0:
#             sum_value += vs[i]
#     return sum_value
#
#
# nums = [1, 2, 3, 4]
# print(sum_odd(nums))

# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]


# def product_of_pairs(vs: list):
#     left = 0
#     right = len(vs) - 1
#     array = []
#     while left <= right:
#         array.append(vs[left] * vs[right])
#         left += 1
#         right -= 1
#
#     return array
#
#
# nums = [1, 2, 3, 4, 5]
# print(product_of_pairs(nums))


# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементо
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# def material_list(vs: list):
#     i = 0
#     while i < len(vs):
#         vs[i] = round(vs[i] % 1, 10)
#         if vs[i] == 0:
#             del vs[i]
#             i -= 1
#
#         i += 1
#     return max(vs) - min(vs)
#
#
# print(material_list([1.1, 1.2, 3.1, 5,6,7,  10.01]))


# Написать программу преобразования десятичного числа в двоичное

# def dec_to_bin(dec_number):
#     if dec_number == 0:
#         return 0
#     if dec_number % 2 == 0:
#         return 0 + 10 * dec_to_bin(dec_number // 2)
#     else:
#         return 1 + 10 * dec_to_bin(dec_number // 2)
#
#
# print(dec_to_bin(98))





