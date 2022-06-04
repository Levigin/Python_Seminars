# 1.Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и
# содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя
import math

# def get_sequence(nums: list[int]):
#     L = []
#     M = []
#     index = 1
#
#     while index < len(nums):
#         i = index
#         N = nums[:]
#         while i < len(N) - 1:
#             if N[i] < N[i + 1]:
#                 M.append(N[i])
#                 i += 1
#             else:
#                 N.pop(i + 1)
#         index += 1
#         if len(L) < len(M):
#             L = M
#         M = []
#     if nums[-1] > L[-1]:
#         L.append(nums[-1])
#     if nums[0] < L[0]:
#         L.insert(0, nums[0])
#     return nums
#
#
# print(get_sequence([5, 2, 3, 4, 6, 1, 7]))
# from random import randint
#
# 2.Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.
# def create_file():
#     list_new = ''
#     with open('text_for_task2_in_seminar_4.txt', 'w') as file:
#         for i in range(100):
#             if i != 99:
#                 list_new += str(randint(1, 100)) + ' '
#             else:
#                 list_new += str(randint(1, 100))
#
#         file.write(list_new)
#
#     file.close()
#
#     with open('text_for_task2_in_seminar_4.txt', 'r') as file:
#         list_old = map(int, file.read().split(' '))
#         print(list_old)
#     list_old1 = sorted(list_old)
#
#     return list_old1
#
#
# print(create_file())


# 3.Задача: найти триплеты и просто выводить их на экран.

# def find_triplets(nums):
#     triplet_count = 0
#     final_temp_list = []
#     for i in range(0, len(nums) - 1):
#         s = set()
#         temp_list = []
#         temp_list.append(nums[i])
#         curr_k = -nums[i]
#
#         for j in range(i + 1, len(nums)):
#             if (curr_k - nums[j]) in s:
#                 triplet_count += 1
#                 temp_list.append(nums[j])
#                 temp_list.append(curr_k - nums[j])
#                 final_temp_list.append(tuple(temp_list))
#                 temp_list.pop(2)
#                 temp_list.pop(1)
#
#             s.add(nums[j])
#
#     return final_temp_list
#
#
# def get_triplets_for_file():
#     with open('text_for_task3_in_seminar_4.txt', 'r') as file:
#         list_numbers = list(map(int, file.read().splitlines()))
#         new_list = find_triplets(list_numbers)
#     return new_list
#
#
# print(get_triplets_for_file())

# nums = [1, 2, -3, 4, 5, 6, 7, -8, 9, 10]
# print(find_triplets(nums))




