# # Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д
# for i in range(0, 10):
#     result = (-3) ** i
#     print(result, end=" ")


# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# #n = int(input("Enter the value: "))
# dict1 = {}
# for i in range(1, n + 1):
#     dict1[i] = 3 * i + 1

#print(dict1)


# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
#
str1 = input("Enter the first string: ")  # Hello
str2 = input("Enter the second string: ")  # el
count = 0
for i in str1:
    if i in str2:
        count += 1
print(count)

#Подсчитать сумму цифр в вещественном числе.


# x = "1234.1234"
# nums = x.split('.')
# sum = 0
# value = 0
# for i in nums:
#     sum += int(i)
#
# while sum > 0:
#     value += sum % 10
#     sum = (int)(sum / 10)
#
# print(value)


# Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
# list1 = []
# n = 4
# sum = 1
# for i in range(1, n + 1):
#     sum *= i
#     list1.append(sum)
#
# print(list1)
