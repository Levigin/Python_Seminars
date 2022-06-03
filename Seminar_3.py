# Найти НОК двух чисел

# 1.def smallest_common_multiple(n: int, m: int):
#
#     def gcd(n: int, m: int):
#         if m == 0:
#             return n
#         return gcd(m, n % m)
#
#     return int((n * m)/gcd(m, n))
#
#
# print(smallest_common_multiple(36, 93))


# 2.Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
# import math
#
#
# def get_pi(d: float):
#     i = 0
#     while d < 1:
#         d *= 10
#         i += 1
#
#     pi = round(2 * math.acos(0.0), i)
#     return pi
#
#
# print(get_pi(0.00000000000000001))

# 3.Составить список простых множителей натурального числа N

# def get_simple_numbers(n: int):
#     list_simple_numbers = []
#     for i in range(1, int(n**0.5)):
#         if n % i == 0:
#             list_simple_numbers.append(i)
#
#     return list_simple_numbers
#
#
# print(get_simple_numbers(10000))


# 4.Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности

# def get_list_without_repeat_numbers(nums: list):
#     new_list = []
#     for i in range(len(nums)):
#         if nums[i] not in new_list:
#             new_list.append(nums[i])
#
#     return new_list
#
#
# print(get_list_without_repeat_numbers([1, 1, 2, 6, 8, 8, 4, 3, 2, 2]))


# 5.Дан текстовый файл, содержащий целые числа.Удалить из него все четные числа.

def del_even_numbers():
    list_odd = []
    with open('text_for_task5_in_seminar_3.txt', 'r') as file:
        list_file = file.read().split(' ')
        print(type(list_file[0]))
        for i in range(len(list_file)):
            if int(list_file[i]) % 2 != 0:
                list_odd.append(list_file[i])

    file.close()

    with open('text_for_task5_in_seminar_3.txt', 'w') as file_write:
        file_write.write(str(list_odd))


del_even_numbers()

